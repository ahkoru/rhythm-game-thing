from sprites import *
from main import Game, Button, PgDebug

class Menus:
    def __init__(self, game_instance: Game):
        self.game = game_instance
        self.display = pygame.display.get_surface()
        
        #? Loading stuff
        self.button = Button(self.game.main_menu_sprites, "assets/Kirb.png", True, (WINDOW_WIDTH/2, WINDOW_LENGTH/2))
        self.debug = PgDebug()
        self.debug.debugging = True
    
    def main_menu(self):
        while True:
            #? Game clock
            dt = self.game.clock.tick() / 1000
            
            #? Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.is_clicked() and pygame.mouse.get_pressed()[0]:
                        self.play()

            #? Updates
            self.game.main_menu_sprites.update(dt)
                
            #? Draw
            self.display.fill('black')
            self.game.main_menu_sprites.draw(self.display)
       
            pygame.display.flip()
    
    def play(self):
        running = True
        self.game.import_map()
        self.game.load_map()
        self.game.load_time = pygame.time.get_ticks()
        self.game.music.play()
        while running:
            dt = self.game.clock.tick() / 1000
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.game.pressed(event)
                    
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            #? Update
            self.game.place_notes()
            self.game.note_sprites.update(dt)
            
            #? Draw
            self.display.fill('blue')
            pygame.draw.line(self.display, 'white', (0, LINE_HEIGHT), (WINDOW_WIDTH, LINE_HEIGHT), 10)
            self.game.note_sprites.draw(self.display)
                        
            pygame.display.flip()
            
        self.game.note_sprites.empty()
        self.game.music.stop()