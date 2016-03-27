import pygame
import tile_helper
import resources
import os

class Tile_Editor():
    def __init__(self, screen):
        self.screen = screen
        self.width = 1344
        self.height = 768
        self.wait = 100

        self.box_size = 32
        self.mouse_col = 0
        self.mouse_row = 0
        self.selection = "X"
        
        self.area = tile_helper.Scene(int(resources.width/32), int(resources.height/32))
        self.sidebar = tile_helper.Sidebar(self.width, self.height, self.screen)

        self.next = pygame.time.get_ticks() + self.wait
    
    def draw(self):
        self.sidebar.draw()
        
        for row in range(len(self.area.grid)):
            for column in range(len(self.area.grid[row])):
                if self.area.grid[row][column] == "X":
                    pygame.draw.rect(self.screen, pygame.Color(0, 0, 0, 0), (column * self.box_size, row * self.box_size, self.box_size, self.box_size))
                else:
                    #if self.selection == "X":
                    #    pygame.draw.rect(self.screen, pygame.Color(0, 0, 0, 0), (column * self.box_size, row * self.box_size, self.box_size, self.box_size))
                    #else:
                    self.screen.blit(resources.AllSprites[self.area.grid[row][column]], (column * self.box_size, row * self.box_size, self.box_size, self.box_size))

        self.draw_grid()

    def mouse_update(self):
        if pygame.mouse.get_pos()[0] < resources.width and pygame.mouse.get_pos()[0] > 0 and pygame.mouse.get_pos()[1] < resources.height and pygame.mouse.get_pos()[1] > 0:
            if pygame.mouse.get_pressed()[0]:
                self.mouse_col = pygame.mouse.get_pos()[0] // self.box_size
                self.mouse_row = pygame.mouse.get_pos()[1] // self.box_size
                self.area.edit_tile(self.mouse_col, self.mouse_row, self.selection)
        
        elif (pygame.mouse.get_pos()[0] > resources.width and pygame.mouse.get_pos()[0] < self.width and pygame.mouse.get_pos()[1] < self.height and pygame.mouse.get_pos()[1] > 0):
            if pygame.mouse.get_pressed()[0]:
                self.mouse_col = (pygame.mouse.get_pos()[0] - resources.width) // self.box_size
                self.mouse_row = (pygame.mouse.get_pos()[1] - resources.height) // self.box_size
                self.selection = self.sidebar.get_griditem(self.mouse_col, self.mouse_row)
            
    def key_update(self):
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.wait
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_RETURN]:
                if self.sidebar.column == 0:
                    if self.sidebar.place == 2:
                        self.screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
                        self.area.save()
                        self.screen = pygame.display.set_mode((1344, 768), pygame.FULLSCREEN|pygame.RESIZABLE)
                    
                    elif self.sidebar.place == 1:
                        pass

                    elif self.sidebar.place == 0:
                        return "menu"
                if self.sidebar.column == 1:
                    if self.sidebar.place == 2:
                        self.area.clear()
                    
                    elif self.sidebar.place == 1:
                        pass

                    elif self.sidebar.place == 0:
                        return "menu"

            if keys[pygame.K_UP]:
                self.sidebar.switch_button(pygame.K_UP)
                
            if keys[pygame.K_DOWN]:
                self.sidebar.switch_button(pygame.K_DOWN)

            if keys[pygame.K_RIGHT]:
                self.sidebar.switch_button(pygame.K_RIGHT)
                
            if keys[pygame.K_LEFT]:
                self.sidebar.switch_button(pygame.K_LEFT)
                    
    def draw_grid(self):
        for line in range(1, int(resources.width/32)):
            pygame.draw.line(self.screen, pygame.Color(255,255,255,255), (line * self.box_size, 0), (line * self.box_size, resources.height))

        for line in range(1, int(resources.height/32)):
            pygame.draw.line(self.screen, pygame.Color(255,255,255,255),(0, line * self.box_size), (resources.width, line * self.box_size))

        
