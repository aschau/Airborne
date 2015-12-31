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
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
        self.mode = "menu"
        self.previous = "menu"
        self.clock = pygame.time.Clock()
        self.editor = Tile_Editor(self.screen)
        self.menu = Main_Menu(self.screen)

    def game_loop(self):
        while resources.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    resources.running = False
                    
            if self.mode == "menu":
                if self.previous != "menu":
                    self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
                    self.previous = "menu"

                self.menu.draw()
                selection = self.menu.update()

                if selection == "editor":
                    self.mode = "edit"
                    self.previous = "menu"

                if selection == "exit":
                    resources.running = False

            elif self.mode == "edit":
                if self.previous != "editor":
                    self.screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
                    self.previous = "editor"
                    
                self.editor.draw()
                selection = self.editor.update()

                if selection == "menu":
                    self.mode = "menu"
                    self.previous = "editor"
                
            pygame.display.update()
            self.clock.tick(30)
##            print(self.clock.get_fps())
                
        pygame.quit()        
    
if __name__ == "__main__":
    MainWindow = Airborne()
    MainWindow.game_loop()
