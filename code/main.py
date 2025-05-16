from sprites import *
from functions import read_osu_map
from tkinter.filedialog import askopenfilename
from os import makedirs
from os.path import join, dirname, isfile
import json
import shutil


class Game():
    def __init__(self):
        #? Initialization
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_LENGTH))
        pygame.display.set_caption('lmao nerd')
        
        
        #? Setup
        self.clock = pygame.Clock()
        
        self.is_running = True
        self.is_playing = False
        
        
        #? Loading stuff
        self.kirby_surf = pygame.image.load("assets/Kirb.png").convert_alpha()
        self.font = pygame.Font(None, 50)
        
        
        #? Sprite/Sprite groups
        self.all_sprites = pygame.sprite.Group()
       
       
       #? Notes
        self.notes: dict[str, list[Note]] = {}
        
        
        #? Maps
        self.import_map()
        self.load_map()
        
    
    def import_map(self):
        beatmap_path = askopenfilename()                        #* Absolute path
        self.map_directory = dirname(beatmap_path)              #* Directory of the absolute path
        self.map_title = beatmap_path.split('/')[-2]            #* Title of the map
        self.map_path = join('maps', self.map_title,'map.json') #* Path where the converted map is placed
        pygame.display.set_caption(self.map_title)              #* Change window title to the song title
        
        #? Return if the map already exists in the map path
        if isfile(self.map_path):
            return 
        
        makedirs(join('maps', self.map_title), exist_ok=True)   #* Make the necessary directories
        
        beatmap = read_osu_map(beatmap_path, True)              #* Convert .osu map file to something usable
        
        #? Save it to the maps directory
        with open(self.map_path, 'w', encoding='utf-8') as file:
            json.dump(beatmap, file)
        
        #? Copy the audio to the same directory
        shutil.copyfile(
            join(self.map_directory, 'audio.mp3'),
            join(dirname(self.map_path), 'audio.mp3')
        )
    
    def load_map(self):
        #? Open the saved beatmap
        with open(self.map_path, 'r', encoding='utf-8') as file:
            beatmap = json.load(file)
        
        #? Create Note objects based on the beatmap data
        for lane, y_values in enumerate(beatmap.values(), 1):
            lane_num = f"lane {lane}"
            self.notes[lane_num] = []
            for y in y_values:
                note = Note(self.all_sprites, self.kirby_surf, ((WINDOW_WIDTH / 5) * lane, -y + 500), 1000, self.notes, lane_num)
                self.notes[lane_num].append(note)
        
        #? Load the music
        self.music = pygame.mixer.Sound(join(dirname(self.map_path), 'audio.mp3'))
        self.music.set_volume(0.5)
        self.load_time = pygame.time.get_ticks()

    
    def pressed(self, event: pygame.event.Event):
        #? key name(a,s,j,k)
        key_name = pygame.key.name(event.key)

        match key_name:
            case 'a':
                self.notes["lane 1"][-1].note_hit()
            case 's':
                self.notes["lane 2"][-1].note_hit()
            case 'k':
                self.notes["lane 3"][-1].note_hit()
            case 'l':
                self.notes["lane 4"][-1].note_hit()
            case _:
                pass
    
    #NOTE: for debugging purposes only
    def highlight(self):
        for lane in self.notes.keys():
            pos = self.notes[lane][-1].rect.center
            
            surf = pygame.Surface((100,100))
            surf.fill('grey')
            rect = surf.get_frect(center = pos)
            self.display.blit(surf, rect)
            
            text_surf = self.font.render("Hit me", True, 'white')
            text_rect = text_surf.get_frect(center = pos)
            self.display.blit(text_surf, text_rect)

    def run(self):
        while self.is_running:
            #? Game clock
            dt = self.clock.tick() / 1000
            
            #? Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    self.pressed(event)
            
            if pygame.time.get_ticks() - self.load_time > 500:
                #? Updates
                self.all_sprites.update(dt)
                
                #? Draw
                self.display.fill('black')
                pygame.draw.line(self.display, 'white', (0, LINE_HEIGHT), (WINDOW_WIDTH, LINE_HEIGHT), 10)
                self.all_sprites.draw(self.display)
                self.highlight()

                if not self.is_playing:
                    self.music.play()
                    self.is_playing = True
                
            
            pygame.display.flip()
            
        pygame.quit()
    

if __name__ == '__main__':
    game = Game()
    game.run()