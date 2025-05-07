from settings import *
from random import randint, uniform

class Note(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos, note_speed, notes, lane_num):
        super().__init__(groups)
        
        self.lane_num = lane_num
        self.notes = notes
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.speed = note_speed
        self.direction = pygame.Vector2(0, 1)
        
    def move(self, dt):
        self.rect.center += self.speed * self.direction * dt
        
        if self.rect.top > WINDOW_LENGTH and self.notes[self.lane_num][-1] == self:
            print('missed D:')
            self.notes[self.lane_num].pop()
            self.kill()
            
        
    def note_hit(self, key):
        if self.rect.bottom > WINDOW_LENGTH * 2 / 3:
            print(f'hit! {self.lane_num}')
            self.notes[self.lane_num].pop()
            self.kill()

    def update(self, dt):
        self.move(dt)