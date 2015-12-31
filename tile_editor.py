import pygame
import tile_helper
import resources
import os

class Tile_Editor():
    def __init__(self, screen):
        self.screen = screen
        self.width = 1344
        self.height = 768

        self.box_size = 32
        self.mouse_col = 0
        self.mouse_row = 0
        
        self.area = tile_helper.Scene(int(resources.width/32), int(resources.height/32))
        self.sidebar = tile_helper.Sidebar(self.width, self.height, self.screen)
    
    def draw(self):
        self.draw_grid()
        self.sidebar.draw()
        
        for row in range(len(self.area.grid)):
            for column in range(len(self.area.grid[row])):
                if self.area.grid[row][column] == 'T':
                    self.screen.blit(resources.AllSprites["basic_block.png"], (column * self.box_size, row * self.box_size, self.box_size, self.box_size))

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            if self.sidebar.place == 2:
                pass
            
            elif self.sidebar.place == 1:
                pass

            elif self.sidebar.place == 0:
                return "menu"

        if keys[pygame.K_UP]:
            self.sidebar.switch_button(pygame.K_UP)
            
        if keys[pygame.K_DOWN]:
            self.sidebar.switch_button(pygame.K_DOWN)

        if pygame.mouse.get_pos()[0] < resources.width and pygame.mouse.get_pos()[0] > 0 and pygame.mouse.get_pos()[1] < resources.height and pygame.mouse.get_pos()[1] > 0:
            if pygame.mouse.get_pressed()[0]:
                self.mouse_col = pygame.mouse.get_pos()[0] // self.box_size
                self.mouse_row = pygame.mouse.get_pos()[1] // self.box_size
                self.area.edit_tile(self.mouse_col, self.mouse_row, 'T')

        pygame.time.delay(60)
                    
    def draw_grid(self):
        for line in range(1, int(resources.width/32)):
            pygame.draw.line(self.screen, pygame.Color(255,255,255,255), (line * self.box_size, 0), (line * self.box_size, resources.height))

        for line in range(1, int(resources.height/32)):
            pygame.draw.line(self.screen, pygame.Color(255,255,255,255),(0, line * self.box_size), (resources.width, line * self.box_size))

        
