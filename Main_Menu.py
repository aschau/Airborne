import pygame
import resources

class MainMenu():
    def __init__(self, screen):
        self.start = resources.AllSprites["Menu.png"]
        self.cont = resources.AllSprites["Menu.png"]
        self.exit = resources.AllSprites["Menu.png"]
        self.buttons = [self.start, self.cont, self.exit]
        self.previous = 0
        self.place = 0
        self.active = self.buttons[self.place]
        self.menubarw = 200
        self.menubarh = 60
        self.fontsize = 56
        self.font = pygame.font.Font(pygame.font.match_font('comicsansms'), self.fontsize)
        self.screen = screen
        self.background = resources.AllSprites["rpgworld.png"]
        
    def draw(self):
        self.screen.blit(self.background, (35, 35))
        self.screen.blit(self.buttons[0], (resources.width/2 - self.menubarw/2.8, resources.height/3 + self.menubarh))
        self.screen.blit(self.buttons[1], (resources.width/2 - self.menubarw/2.8, resources.height/2 + self.menubarh))
        self.screen.blit(self.buttons[2], (resources.width/2 - self.menubarw/2.8, resources.height/1.5 + self.menubarh))
        s_title = "RPG World"
        title = self.font.render(s_title, True, pygame.Color(255,255,255))
        self.screen.blit(title, (resources.width/2 - (self.fontsize*len(s_title)/4.2), resources.height/5))

    def update(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    resources.running = False
                    
            #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_w:
            if keys[pygame.K_w]:
                self.previous = self.place
                if self.place != 0:
                    self.place -= 1
                else:
                    self.place = len(self.buttons)-1
                
            #elif event.key == pygame.K_s:
            if keys[pygame.K_s]:
                self.previous = self.place
                if self.place != (len(self.buttons) - 1):
                    self.place += 1
                else:
                    self.place = 0

        self.buttons[self.place] = resources.AllSprites["ActiveMenu.png"]
        self.buttons[self.previous] = resources.AllSprites["Menu.png"]
