import pygame

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


