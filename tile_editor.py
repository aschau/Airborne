import pygame
import resources
import os

class Tile_Editor():
    def __init__(self, screen):
        self.screen = screen
        self.box_size = 32

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_grid()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                resources.running = False
                    
    def draw_grid(self):
        for line in range(1, int(resources.width/32)):
            pygame.draw.line(self.screen, pygame.Color(255,255,255,255), (line * self.box_size, 0), (line * self.box_size, resources.height))

        for line in range(1, int(resources.height/32)):
            pygame.draw.line(self.screen, pygame.Color(255,255,255,255),(0, line * self.box_size), (resources.width, line * self.box_size))
