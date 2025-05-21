from sprites import *
from classes import *
from menus import *
from debug import *


class Game():
    def __init__(self):
        #? Initialization
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_LENGTH))
        pygame.display.set_caption('lmao nerd')
        
        #? Setup
        self.clock = pygame.Clock()
        
        #? Sprite/Sprite groups
        self.main_menu_sprites = pygame.sprite.Group()
        self.note_sprites = pygame.sprite.Group()
       
       #? Notes
        self.notes: dict[str, list[Note]] = {"lane 1":[], "lane 2":[], "lane 3":[], "lane 4":[]}

    def text(self, content):
        pass
    
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
            self.beatmap: dict[str, list[int]] = json.load(file)
        
        #? Create Note objects based on the beatmap data
        # for lane, y_values in enumerate(self.beatmap.values(), 1):
        #     lane_num = f"lane {lane}"
        #     self.notes[lane_num] = []
        #     for y in y_values:
        #         note = Note(self.note_sprites, self.kirby_surf, (WINDOW_WIDTH / 5) * lane, 1000, self.notes, lane_num)
        #         self.notes[lane_num].append(note)
        
        #? Load the music
        self.music = pygame.mixer.Sound(join(dirname(self.map_path), 'audio.mp3'))
        self.music.set_volume(0.5)
        self.load_time = pygame.time.get_ticks()
        if self.load_time > 1000: return

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
    
    def place_notes(self):
        for lane, y_values in enumerate(self.beatmap.values(), 1):
                lane_num = f"lane {lane}"
                if y_values[-1] <= pygame.time.get_ticks() - self.load_time:
                    note = Note(self.note_sprites, self.kirby_surf, (WINDOW_WIDTH / 5) * lane, 1000, self.notes, lane_num)
                    self.notes[lane_num].insert(0, note)
                    self.beatmap[lane_num].pop()
    
    #? for debugging purposes only
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
        self.menus = Menus()
        self.menus.main_menu()
        
if __name__ == '__main__':
    game = Game()
    game.run()