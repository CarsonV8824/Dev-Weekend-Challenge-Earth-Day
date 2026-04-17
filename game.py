import pygame
import random

from sprites.trash import Trash
from sprites.turtle import Turtle

def main():
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

    lives = 3
    font = pygame.font.Font(None, 40)

    while running:
        dt = clock.tick(60)  # dt = time since last frame in milliseconds
        spawn_timer += dt
        
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

        turtle = list(tutrle_group)[0]
        hits = pygame.sprite.spritecollide(turtle, trash_group, False)
        for trash in hits:
            if trash:
                trash.kill()
                lives -= 1
                print("hit!")

        if lives <= 0:
            running = False

        for trash in trash_group:
            trash.update(list(tutrle_group)[0].get_coords())
        tutrle_group.update()
        
        screen.fill("purple")
        trash_group.draw(screen)
        tutrle_group.draw(screen)

        lives_text = font.render(f"lives: {lives}", True, (255,255,255))
        screen.blit(lives_text, (50,50))

        pygame.display.flip()  
if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()