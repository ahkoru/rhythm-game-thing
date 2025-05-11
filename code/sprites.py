from settings import *
from random import randint, uniform

class Note(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos, note_speed, notes, lane_num):
        super().__init__(groups)
        self.pos = pos
        self.lane_num = lane_num
        self.notes = notes
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.speed = note_speed
        self.direction = pygame.Vector2(0, 1)
        
    def move(self, dt):
        self.rect.center += self.speed * self.direction * dt
        
        # if self.rect.top > WINDOW_LENGTH and self.notes[self.lane_num][-1] == self:
        if self.rect.y > LINE_HEIGHT + 100:
            print('missed D:')
            self.notes[self.lane_num].pop()
            self.kill()
            
        
    def note_hit(self):
        time_error = abs(self.rect.centery - LINE_HEIGHT)
        if self.rect.bottom > WINDOW_LENGTH * 2 / 3:
        #     print(f'hit! {self.lane_num}')
        #     self.notes[self.lane_num].pop()
        #     self.kill()

        
        # if self.rect.collidepoint(self.pos[0], LINE_HEIGHT):
        # if self.rect.y > LINE_HEIGHT - 100:
            if time_error < 15:
                print('Perfect')
            elif time_error < 60:
                print('Great')
            elif time_error < 200:
                print('Good')
            else:
                print('eh')
            self.notes[self.lane_num].pop()
            self.kill()
            
            
        
    def update(self, dt):
        self.move(dt)