from sprites import *

class Button(pygame.sprite.Sprite):
    def __init__(self, group, image, transparent, pos):
        super().__init__(group)
        if transparent:
            self.image = pygame.image.load(image).convert_alpha()
        else:
            self.image = pygame.image.load(image).convert()
            
        self.rect = self.image.get_frect(center = pos)
    
    def is_clicked(self):
        mx, my = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mx, my):
            return True
        else:
            return False
    
    # def drag(self, first_time):
    #     if first_time:
    #         pygame.mouse.set_pos(self.rect.center)
    #         return False
    #     self.rect.center = pygame.mouse.get_pos()

# class Map:
#     def __init__(self):
#         pass
    
#     def import_map(self):
#         beatmap_path = askopenfilename()                        #* Absolute path
#         self.map_directory = dirname(beatmap_path)              #* Directory of the absolute path
#         self.map_title = beatmap_path.split('/')[-2]            #* Title of the map
#         self.map_path = join('maps', self.map_title,'map.json') #* Path where the converted map is placed
#         pygame.display.set_caption(self.map_title)              #* Change window title to the song title
        
#         #? Return if the map already exists in the map path
#         if isfile(self.map_path):
#             return 
        
#         makedirs(join('maps', self.map_title), exist_ok=True)   #* Make the necessary directories
        
#         beatmap = read_osu_map(beatmap_path, True)              #* Convert .osu map file to something usable
        
#         #? Save it to the maps directory
#         with open(self.map_path, 'w', encoding='utf-8') as file:
#             json.dump(beatmap, file)
        
#         #? Copy the audio to the same directory
#         shutil.copyfile(
#             join(self.map_directory, 'audio.mp3'),
#             join(dirname(self.map_path), 'audio.mp3')
#         )
    
#     def load_map(self):
#         #? Open the saved beatmap
#         with open(self.map_path, 'r', encoding='utf-8') as file:
#             beatmap = json.load(file)
        
#         #? Create Note objects based on the beatmap data
#         for lane, y_values in enumerate(beatmap.values(), 1):
#             lane_num = f"lane {lane}"
#             self.notes[lane_num] = []
#             for y in y_values:
#                 note = Note(self.note_sprites, self.kirby_surf, ((WINDOW_WIDTH / 5) * lane, -y), 1000, self.notes, lane_num)
#                 self.notes[lane_num].append(note)
        
#         #? Load the music
#         self.music = pygame.mixer.Sound(join(dirname(self.map_path), 'audio.mp3'))
#         self.music.set_volume(0.5)
#         self.load_time = pygame.time.get_ticks()
#         if self.load_time > 1000: return
        
    