import pygame
import random
import math
import json
import os

from sprites.trash import Trash
from sprites.turtle import Turtle
from sprites.player import Player 

from data.state import state
from data.database import Database

from oceans.facts import fact_for_pacific

# Get project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def pacific(game_state:dict) -> dict:
    pygame.init()
    info = pygame.display.Info()
    SCREEN_WIDTH = info.current_w
    SCREEN_HEIGHT = info.current_h
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Franklin and the Diver")
    
    # Set window icon
    icon_path = os.path.join(PROJECT_ROOT, "assets", "Net.png")
    if os.path.exists(icon_path):
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
    path = os.path.join(PROJECT_ROOT, "oceans", "json", "pacific.json")
    with open(path, "r") as f:
        screen_colors = json.load(f)
    clock = pygame.time.Clock()
    running = True

    spawn_timer = 0
    spawn_interval = 1000  # milliseconds
    trash_group = pygame.sprite.Group()

    turtle_group = pygame.sprite.Group()
    turtle = Turtle(SCREEN_WIDTH//1.2, SCREEN_HEIGHT//2)
    turtle_group.add(turtle)

    player_group = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    player_group.add(player)

    font = pygame.font.Font(None, 40)

    lives = game_state["lives"] if game_state else 3
    score = game_state["score"] if game_state else 0
    pacific_wins = game_state["pacific_wins"] if game_state else 0

    wave = 1
    wave_timer = 0
    wave_interval = 15000

    # For displaying facts without freezing
    showing_fact = False
    fact_timer = 0
    fact_duration = 5000  # 5 seconds in milliseconds
    current_fact = ""

    win = False

    closed = False
    while running:
        dt = clock.tick(60)  # dt = time since last frame in milliseconds
        spawn_timer += dt if not showing_fact else 0
        wave_timer += dt if not showing_fact else 0
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT: 
                    running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            running = False
                            closed = True
        
        # Spawn every 2 seconds consistently
        if spawn_timer >= spawn_interval and not showing_fact:
            trash = Trash(0, random.randint(0, SCREEN_HEIGHT), 45)
            trash_group.add(trash)
            spawn_timer = 0  # Reset timer
            

        turtle = list(turtle_group)[0]
        hits = pygame.sprite.spritecollide(turtle, trash_group, True)
        for trash in hits:
            if trash:
                lives -= 1
                print("hit!")

        temp_player = list(player_group)[0]
        player_hit = pygame.sprite.spritecollide(temp_player, trash_group, False)

        # Handle player catching trash
        if player_hit:
            for trash in player_hit:
                score += 1
                trash_group.remove(trash)
                print("Caught trash!")

        if lives <= 0:
            running = False

        if wave >= 4:
            win = True
            running = False

        # Only update trash if not showing a fact
        if not showing_fact:
            for trash in trash_group:
                trash.update(list(turtle_group)[0].get_coords())
        turtle_group.update()
        
        # Update player with screen boundaries
        for player in player_group:
            player.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Update fact timer if currently showing a fact
        if showing_fact:
            fact_timer += dt
            if fact_timer >= fact_duration:
                showing_fact = False
                fact_timer = 0
        
        screen.fill("purple")
        stripe_height = SCREEN_HEIGHT // len(screen_colors)
        y_pos = 0
        for row in screen_colors:
            pygame.draw.rect(screen, (row[1], row[2], row[3]), rect=(0, y_pos, SCREEN_WIDTH, stripe_height))
            y_pos += stripe_height

        trash_group.draw(screen)
        turtle_group.draw(screen)
        player_group.draw(screen)

        lives_text = font.render(f"lives: {lives}", True, (255,255,255))
        screen.blit(lives_text, (50,50))

        wave_on_text = font.render(f"wave: {wave}", True, (255, 255, 255))
        screen.blit(wave_on_text, (200, 50))

        score_text = font.render(f"score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (350, 50))

        pacific_wins_text = font.render(f"pacific wins: {pacific_wins}", True, (255, 255, 255))
        screen.blit(pacific_wins_text, (650, 50))

        time_left_text = font.render(f"Time left: {math.ceil(math.ceil(wave_interval-wave_timer)/1000)}", True, (255,255,255))
        screen.blit(time_left_text, (1050, 50))

        
        if wave_timer >= wave_interval:
            wave_interval += 5000
            wave += 1
            wave_timer = 0
            showing_fact = True
            fact_timer = 0
            current_fact = fact_for_pacific()
        
        # Display fact if currently showing one
        if showing_fact:
            fun_fact_text = font.render(f"Fact: {current_fact}", True, (255,255,255))
            text_rect = fun_fact_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(fun_fact_text, text_rect)
        
        pygame.display.flip()  

    if win:
        # add to stats
        game_state["score"] += score
        game_state["lives"] = lives
        game_state["pacific_wins"] += 1
    if not win and not closed:
        # reset stats because you lost
        game_state["score"] = 0
        game_state["lives"] = 3
        game_state["pacific_wins"] = 0
    print(game_state)
    Database.insert_data(game_state)
    pygame.quit()
    