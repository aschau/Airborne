import pygame
import scene
import resources
import os

class Tile_Editor():
    def __init__(self, screen):
        self.screen = screen

        self.box_size = 32
        self.mouse_col = 0
        self.mouse_row = 0
        
        self.area = scene.Scene(int(resources.width/32), int(resources.height/32))
        

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_grid()

        for row in range(len(self.area.grid)):
            for column in range(len(self.area.grid[row])):
                if self.area.grid[row][column] == 'T':
                    pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255), (column * self.box_size, row * self.box_size, self.box_size, self.box_size))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                resources.running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    resources.running = False

            if pygame.mouse.get_pressed()[0]:
                self.mouse_col = pygame.mouse.get_pos()[0] // self.box_size
                self.mouse_row = pygame.mouse.get_pos()[1] // self.box_size
                self.area.edit_tile(self.mouse_col, self.mouse_row, 'T')
                    
    def draw_grid(self):
        for line in range(1, int(resources.width/32)):
            pygame.draw.line(self.screen, pygame.Color(255,255,255,255), (line * self.box_size, 0), (line * self.box_size, resources.height))

        for line in range(1, int(resources.height/32)):
            pygame.draw.line(self.screen, pygame.Color(255,255,255,255),(0, line * self.box_size), (resources.width, line * self.box_size))
