import os, sys
import pygame
from pygame.locals import *
import resources
from Main_Menu import *

if not pygame.font:
    print('Warning, fonts disabled')

if not pygame.mixer:
    print('Warning, sound disabled')

class RPGMain:
    def __init__(self):
        pygame.init()
        self.width = resources.width
        self.height = resources.height
##        self.fullscreen = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        #self.running = True
        self.menu = MainMenu(self.screen)

    def game_loop(self):
        while resources.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    resources.running = False
                    
##                elif event.type == pygame.KEYDOWN:
##                    if event.key == pygame.K_BACKQUOTE:
##                        try:
##                            if not self.fullscreen:
##                                self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
##                                self.fullscreen = True
##
##                            else:
##                                self.screen = pygame.display.set_mode((self.width, self.height))
##                                self.fullscreen = False
##                        except:
##                            pass
            self.menu.draw()
            self.menu.update()
            pygame.display.update()
                
        pygame.quit()        
    
if __name__ == "__main__":
    MainWindow = RPGMain()
    MainWindow.game_loop()
