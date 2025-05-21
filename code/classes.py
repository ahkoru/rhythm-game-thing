from sprites import *

class Button(pygame.sprite.Sprite):
    def __init__(self, group, image, transparent, pos):
        super().__init__(group)
        if image is None:
         self.image = pygame.Surface(50, 50)
         self.image = pygame.draw.rect(self.image, )
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
    

