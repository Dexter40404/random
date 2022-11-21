import pygame
import os, math



os.chdir(os.path.dirname(os.path.abspath(r"C:\Users\Dexter\PycharmProjects\start\main.py")))


class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.W, self.H = 1280, 600
        self.screen = pygame.Surface((self.W, self.H))
        self.window = pygame.display.set_mode((self.W, self.H))
        self.background = self.window.fill((0, 0, 0))
        self.playerX, self.playerY, self.playerX_change, self.playerY_change, self.playerY2 = 600, 360, 0, 0, 360
        self.playerimg = pygame.image.load("player666.png")
        self.playerimg = pygame.transform.scale(self.playerimg, (
        int(self.playerimg.get_height() / 2), (self.playerimg.get_width() / 2)))
        self.player_rect = self.playerimg.get_rect()
        self.enemyX, self.enemyY, self.enemyX_change, self.enemyY_change = 900, 360, 0, 0
        self.bulletX, self.bulletY, self.bulletX_change, self.bulletY_change = 20, 0, 1, 0.2
        self.bulletimg = pygame.image.load("rose.png")
        self.bullet_rect = self.bulletimg.get_rect()
        self.bullet_state = "ready"

    def player(self):
        self.screen.blit(self.playerimg, (self.playerX, self.playerY))

    def enemy(self):
        self.screen.blit(self.playerimg, (self.enemyX, self.enemyY))

    def bullet_fire(self, x, y):
        self.bullet_state = "fire"
        self.screen.blit(self.bulletimg, (x + 80, y + 40))





    def game_loop(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.borders()
            self.gravity()
            self.player()
            self.enemy()
            self.movement()
            self.isCollision()
            self.bullet_dis()
            self.window.blit(self.screen, (0, 0))
            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
        exit()

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.playerX_change = 0
                if event.key == pygame.K_a:
                    self.playerX_change = 0
                if event.key == pygame.K_SPACE:
                    self.playerY_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.playerY_change = - 10
                if event.key == pygame.K_RETURN:
                    self.bulletX += self.bulletX_change
                    self.bullet_fire(self.playerX, self.playerY)


        self.playerX += self.playerX_change
        self.playerY += self.playerY_change
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.playerX_change = - 2
        if keys[pygame.K_d]:
            self.playerX_change = 2



    def gravity(self):
        self.playerY_change += 0.2

    def borders(self):
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 1075:
            self.playerX = 1075
        elif self.playerY >= 395:
            self.playerY = 395
        if self.bulletX >=1075:
            self.bullet_state = "ready"
        elif self.bulletY >=395:
            self.bullet_state = "ready"

    def isCollision(self):
        distance = math.sqrt((math.pow(self.enemyX - self.bulletX, 2)) + (math.pow(self.enemyY - self.bulletY, 2)))
        if distance < 60:
            return True
        else:
            return False

    def bullet_dis(self):
        if self.isCollision() == True:
            self.bullet_state = "ready"









g = Game()

while g.running:
    g.game_loop()
