import pygame
import random
import time
import math

from sprites.trash import Trash
from sprites.turtle import Turtle
from sprites.player import Player 

def alantic() -> dict:
    info = pygame.display.Info()
    SCREEN_WIDTH = info.current_w
    SCREEN_HEIGHT = info.current_h
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    spawn_timer = 0
    spawn_interval = 2000  # milliseconds

    trash_group = pygame.sprite.Group()

    tutrle_group = pygame.sprite.Group()
    turtle = Turtle(SCREEN_WIDTH//1.2, SCREEN_HEIGHT//2)
    tutrle_group.add(turtle)

    player_group = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    player_group.add(player)

    font = pygame.font.Font(None, 40)

    lives = 3
    score = 0

    wave = 1
    wave_timer = 0
    wave_interval = 15000

    win = False

    while running:
        dt = clock.tick(60)  # dt = time since last frame in milliseconds
        spawn_timer += dt
        wave_timer += dt
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT: 
                    running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            running = False
        
        # Spawn every 2 seconds consistently
        if spawn_timer >= spawn_interval:
            trash = Trash(0, random.randint(0, SCREEN_HEIGHT), 45)
            trash_group.add(trash)
            spawn_timer = 0  # Reset timer

        if wave_timer >= wave_interval:
            wave_interval += 5000
            wave += 1
            wave_timer = 0
            time.sleep(5)
            

        turtle = list(tutrle_group)[0]
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
                trash_group.remove(trash)
                print("Caught trash!")

        if lives <= 0:
            running = False

        if wave >= 4:
            win = True
            running = False

        for trash in trash_group:
            trash.update(list(tutrle_group)[0].get_coords())
        tutrle_group.update()
        
        # Update player with screen boundaries
        for player in player_group:
            player.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        screen.fill("purple")
        trash_group.draw(screen)
        tutrle_group.draw(screen)
        player_group.draw(screen)

        lives_text = font.render(f"lives: {lives}", True, (255,255,255))
        screen.blit(lives_text, (50,50))

        wave_on_text = font.render(f"wave: {wave}", True, (255, 255, 255))
        screen.blit(wave_on_text, (200, 50))

        time_left_text = font.render(f"Time left: {math.ceil(math.ceil(wave_interval-wave_timer)/1000)}", True, (255,255,255))
        screen.blit(time_left_text, (350, 50))

        pygame.display.flip()  

    if win:
        score = score
    if not score:
        score = 0
    
    return {"score":score, "lives":lives, "win":win}

if __name__ == "__main__":
    pygame.init()
    alantic()
    pygame.quit()