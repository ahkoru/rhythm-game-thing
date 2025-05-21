from sprites import *
from main import Game

class Menus(Game):
    def __init__(self):
        super().__init__()
    
    def main_menu(self):
        while True:
            #? Game clock
            dt = self.clock.tick() / 1000
            
            #? Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.is_clicked() and pygame.mouse.get_pressed()[0]:
                        self.play()

            #? Updates
            self.main_menu_sprites.update(dt)
                
            #? Draw
            self.display.fill('black')
            self.main_menu_sprites.draw(self.display)
       
            pygame.display.flip()
    
    def play(self):
            running = True
            self.import_map()
            self.load_map()
            self.load_time = pygame.time.get_ticks()
            self.music.play()
            while running:
                dt = self.clock.tick() / 1000
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        self.pressed(event)
                        
                        if event.key == pygame.K_ESCAPE:
                            running = False
                
                #? Update
                self.place_notes()
                self.note_sprites.update(dt)
                
                #? Draw
                self.display.fill('blue')
                pygame.draw.line(self.display, 'white', (0, LINE_HEIGHT), (WINDOW_WIDTH, LINE_HEIGHT), 10)
                self.note_sprites.draw(self.display)
                self.debug.debug(str(pygame.mouse.get_pos()))
                            
                pygame.display.flip()
                
            self.note_sprites.empty()
            self.music.stop()