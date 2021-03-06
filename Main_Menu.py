import pygame
import resources

class Main_Menu():
    def __init__(self, screen):
        self.title = "Airborne"

        self.sbutton = "Start"
        self.cbutton = "Continue"
        self.sebutton = "Settings"
        self.ebutton = "Exit"
        self.textbuttons = [self.sbutton, self.cbutton, self.sebutton, self.ebutton]

        self.start = resources.AllSprites["ActiveMenu.png"]
        self.cont = resources.AllSprites["Menu.png"]
        self.settings = resources.AllSprites["Menu.png"]
        self.exit = resources.AllSprites["Menu.png"]
        self.editor = resources.AllSprites["Menu.png"]
        self.buttons = [self.start, self.cont, self.settings, self.exit,]

        self.previous = 0
        self.place = 0
        self.active = self.buttons[self.place]

        self.menubarw = 200
        self.menubarh = 60

        self.tfontsize = 56
        self.tfont = pygame.font.Font(pygame.font.match_font('cooperblack'), self.tfontsize)

        self.bfontsize = 28
        self.bfont = pygame.font.Font(pygame.font.match_font('cooperblack'), self.bfontsize)

        self.screen = screen
        self.background = resources.AllSprites["Main Menu.png"]
        self.wait = 100

        self.next = pygame.time.get_ticks() + self.wait
        
    def draw(self):
        self.screen.blit(self.background, (0, 0))

        for button in range(len(self.buttons)):
            self.screen.blit(self.buttons[button], (resources.width/2 - self.menubarw/2, resources.height/2 + (self.menubarh * button)))
            self.screen.blit(self.bfont.render(self.textbuttons[button], True, pygame.Color(255,255,255)), (resources.width/2 - self.menubarw/2 + 5, resources.height/2 + (self.menubarh * button)))

        self.screen.blit(self.tfont.render(self.title, True, pygame.Color(255,255,255)), (resources.width/2 - (self.tfontsize*len(self.title)/4.2), resources.height/5))

    def update(self):
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.wait
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.previous = self.place
                if self.place != 0:
                    self.place -= 1
                else:
                    self.place = len(self.buttons)-1

                self.buttons[self.place] = resources.AllSprites["ActiveMenu.png"]
                self.buttons[self.previous] = resources.AllSprites["Menu.png"]
                
            if keys[pygame.K_s]:
                self.previous = self.place
                if self.place != (len(self.buttons) - 1):
                    self.place += 1
                else:
                    self.place = 0

                self.buttons[self.place] = resources.AllSprites["ActiveMenu.png"]
                self.buttons[self.previous] = resources.AllSprites["Menu.png"]

            if keys[pygame.K_RETURN]:
                if self.place == 0:
                    pass
                
                elif self.place == 1:
                    pass

                elif self.place == 2:
                    pass
                
                elif self.place == 3:
                    return "exit"