import pygame


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480


class Player(object):
    IMAGES_WIDTH = 62 # 415
    IMAGES_HEIGHT = 76 # 507
    IMAGES_HIT_WIDTH = 48  # 48 is idle width
    IMAGES_HIT_HEIGHT = 68
    images_idle = [pygame.image.load('res/Idle__000.png'), pygame.image.load('res/Idle__001.png'),
                   pygame.image.load('res/Idle__002.png'), pygame.image.load('res/Idle__003.png'),
                   pygame.image.load('res/Idle__004.png'), pygame.image.load('res/Idle__005.png'),
                   pygame.image.load('res/Idle__006.png'), pygame.image.load('res/Idle__007.png'),
                   pygame.image.load('res/Idle__008.png')]
    images_walk_right = [pygame.image.load('res/Run_Right__000.png'), pygame.image.load('res/Run_Right__001.png'),
                         pygame.image.load('res/Run_Right__002.png'), pygame.image.load('res/Run_Right__003.png'),
                         pygame.image.load('res/Run_Right__004.png'), pygame.image.load('res/Run_Right__005.png'),
                         pygame.image.load('res/Run_Right__006.png'), pygame.image.load('res/Run_Right__007.png'),
                         pygame.image.load('res/Run_Right__008.png')]
    images_walk_left = [pygame.image.load('res/Run_Left__000.png'), pygame.image.load('res/Run_Left__001.png'),
                        pygame.image.load('res/Run_Left__002.png'), pygame.image.load('res/Run_Left__003.png'),
                        pygame.image.load('res/Run_Left__004.png'), pygame.image.load('res/Run_Left__005.png'),
                        pygame.image.load('res/Run_Left__006.png'), pygame.image.load('res/Run_Left__007.png'),
                        pygame.image.load('res/Run_Left__008.png')]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = self.IMAGES_WIDTH
        self.height = self.IMAGES_HEIGHT
        self.vel = 5
        self.is_jumping = False
        self.is_left = False
        self.is_right = False
        self.idleCount = 0
        self.walkCount = 0
        self.jumpCount = 10
        self.is_standing = True
        self.hitbox = (self.x + 0, self.y + 0, self.IMAGES_HIT_WIDTH, self.IMAGES_HEIGHT-2)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.is_standing):
            if self.is_left:
                win.blit(self.images_walk_left[self.walkCount//3], (self.x,self.y))
            elif self.is_right:
                win.blit(self.images_walk_right[self.walkCount//3], (self.x,self.y))
        else:
            '''
            if self.is_right:
                win.blit(self.images_walk_right[0], (self.x, self.y))
            else:
                win.blit(self.images_walk_left[0], (self.x, self.y))
            '''
            win.blit(self.images_idle[self.walkCount // 3], (self.x, self.y))

        self.walkCount += 1

        # draw hit box
        self.hitbox = (self.x + 0, self.y + 0, self.IMAGES_HIT_WIDTH, self.IMAGES_HEIGHT-2)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


clock = pygame.time.Clock()

pygame.init()

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Loot Grab")


def redraw_game_window():

    # draw background
    pygame.draw.rect(win, (175,225,240), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))

    # draw characters
    player.draw(win)
    # goblin.draw(win)

    # draw bullets
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    player = Player(200, 300)
    bullets = []

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
