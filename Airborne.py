import os, sys
import pygame
from pygame.locals import *
import resources
from Main_Menu import *
from tile_editor import *

if not pygame.font:
    print('Warning, fonts disabled')

if not pygame.mixer:
    print('Warning, sound disabled')

class Airborne:
    def __init__(self):
        pygame.init()
        self.width = resources.width
        self.height = resources.height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.menu = Main_Menu(self.screen)
        self.editor = Tile_Editor(self.screen)
        self.mode = "menu"

    def game_loop(self):
        while resources.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    resources.running = False
                    
            if self.mode == "menu":
                self.menu.draw()
                selection = self.menu.update()

                if selection == "editor":
                    self.mode = "edit"

            elif self.mode == "edit":
                self.editor.draw()
                self.editor.update()
                
            pygame.display.update()
                
        pygame.quit()        
    
if __name__ == "__main__":
    MainWindow = Airborne()
    MainWindow.game_loop()
