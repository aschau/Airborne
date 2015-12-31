import resources
import pygame
import os

class Scene():
    def __init__(self, columns, rows):
        self.cols = columns
        self.rows = rows
        self.grid = []
        for row in range(self.rows):
            self.grid.append(self.add_row(self.cols))

    def edit_tile(self, column, row, item):
        self.grid[row][column] = item

    def add_row(self, size):
        row = []
        for space in range(size):
            row.append("X")
        return row

    def save(self):
        fname = input("File name: ")
        file = open(fname, 'w')

        for row in self.grid:
            line = ""

            for char in row:
                line += char
                file.write(line)

        file.close()

class Sidebar():
    def __init__(self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        
        self.sbutton = "Save"
        self.ibutton = "Import"
        self.ebutton = "Exit"
        self.textbuttons = [self.ebutton, self.ibutton, self.sbutton]

        self.save = resources.AllSprites["ActiveMenu.png"]
        self.imp = resources.AllSprites["Menu.png"]
        self.exit = resources.AllSprites["Menu.png"]
        
        self.buttons = [self.exit, self.imp, self.save]

        self.menubarw = 200
        self.menubarh = 60

        self.bfontsize = 28
        self.bfont = pygame.font.Font(pygame.font.match_font('comicsansms'), self.bfontsize)

        self.previous = 2
        self.place = 2
        self.active = self.buttons[self.place]

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color(166, 166, 166, 166), (resources.width, 0, self.width-resources.width, self.height))

        for button in range(len(self.buttons)):
            self.screen.blit(self.buttons[button], (resources.width + (self.width - resources.width)/2 - self.menubarw/2, self.height -  self.menubarh * (button + 1)))
            self.screen.blit(self.bfont.render(self.textbuttons[button], True, pygame.Color(255,255,255)), (resources.width + (self.width - resources.width)/2 - self.menubarw/2 + 5, self.height -  self.menubarh * (button + 1)))

    def switch_button(self, direction):
        self.previous = self.place

        if direction == pygame.K_UP:
            if self.place == len(self.buttons) - 1:
                self.place = 0
            else:
                self.place += 1

        elif direction == pygame.K_DOWN:
            if self.place == 0:
                self.place = len(self.buttons) - 1
            else:
                self.place -= 1

        self.buttons[self.place] = resources.AllSprites["ActiveMenu.png"]
        self.buttons[self.previous] = resources.AllSprites["Menu.png"]
