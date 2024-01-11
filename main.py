import pygame

from constants import *
from Player import *
from Projectile import *
from Level import *



clock = pygame.time.Clock()

pygame.init()

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Loot Grab")


def redraw_game_window():

    # draw background
    pygame.draw.rect(win, (175,225,240), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))

    # draw level
    for level in levels:
        level.draw(win)

    # draw characters
    player.draw(win)
    # goblin.draw(win)

    # draw bullets
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # set up the player
    player = Player(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 80)
    bullets = []

    # set up the levels
    levels = []
    colour = (50, 75, 175)
    colour = (100, 150, 200)
    level = Level(2, 5, colour)
    levels.append(level)

    level.foo()

    run = True
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if player.is_left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:
                bullets.append(
                    Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, (0, 0, 0), facing))

        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
            player.is_left = True
            player.is_right = False
            player.is_standing = False
        elif keys[pygame.K_RIGHT] and player.x < WINDOW_WIDTH - player.width - player.vel:
            player.x += player.vel
            player.is_right = True
            player.is_left = False
            player.is_standing = False
        else:
            player.is_standing = True
            player.walkCount = 0

        if not player.is_jumping:
            if keys[pygame.K_UP]:
                player.is_jumping = True
                player.is_right = False
                player.is_left = False
                player.walkCount = 0
        else:
            if player.jumpCount >= -10:
                neg = 1
                if player.jumpCount < 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) * 0.5 * neg
                player.jumpCount -= 1
            else:
                player.is_jumping = False
                player.jumpCount = 10

        redraw_game_window()
    
    pygame.quit()
