import random
import pygame
import sys

pygame.init()


class My:
    def __init__(self, screen):
        self.w = None
        self.h = None
        self.screen = screen
        self.my = pygame.image.load('./image/木鱼.png')
        self.my_rect = self.my.get_rect()
        self.my_rect.center = self.my_rect.topleft

    def display(self):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.screen.blit(self.my, ((self.w - 311) / 2, (self.h - 263) / 2))


class Game:
    def __init__(self):
        self.y = None
        self.x = None
        self.font_surface_2 = None
        self.mods = pygame.RESIZABLE
        self.screen = pygame.display.set_mode((800, 480), self.mods)
        pygame.display.set_caption('by Cloud sky', 'by Cloud sky')

        self.color_w = [(255, 159, 243), (95, 39, 205), (84, 160, 255), (0, 210, 211), (29, 209, 161), (72, 219, 251),
                        (255, 107, 107), (255, 107, 107), (254, 202, 87), (255, 159, 243)]
        self.color = random.choice(self.color_w)
        self.clock = pygame.time.Clock()

        self.a = 0

        self.screen.fill(self.color)
        pygame.display.flip()

    def key(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            if pygame.display.get_active():
                self.screen.fill(random.choice(self.color_w))
                pygame.mixer.music.load("./music/敲击木鱼.wav")
                pygame.mixer.music.queue('./music/支付宝到账.mp3')
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()
                self.x, self.y = pygame.mouse.get_pos()
                self.screen.blit(self.font_surface_2, (self.x - 20, self.y - 25))
                self.a += 1

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_F11 and self.mods == pygame.RESIZABLE and \
        #         pygame.display.get_active():
        #     self.mods = pygame.FULLSCREEN
        #     self.screen = pygame.display.set_mode((800, 480), self.mods)

    def font(self):
        font = pygame.font.Font('./font/MiSans-Light.ttf', 40)
        font_surface = font.render('当前功德：%d' % self.a, True, 'white')
        self.screen.blit(font_surface, (10, 1))
        font_2 = pygame.font.Font('./font/MiSans-Light.ttf', 20)
        self.font_surface_2 = font_2.render('功德+1', True, 'white')

    def display(self):
        my = My(self.screen)
        while True:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.key(event)
            self.font()
            my.display()

            pygame.display.update()

            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.display()
