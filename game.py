import pygame
from pygame import *
import random

# Initiation de la partie
pygame.init()
# Titre du jeu
pygame.display.set_caption("Shoot'em up 1.0")
# Dimensions de l'aire de jeu 
ecran = pygame.display.set_mode([800, 600])
# gestion de l'horloge du jeu
clock = pygame.time.Clock()
# Gestion de l'apparition des ennemis
Have_ennemy = pygame.USEREVENT + 1
pygame.time.set_timer(Have_ennemy, 500)
# Gestion de l'apparition des étoiles
Have_star = pygame.USEREVENT + 2
pygame.time.set_timer(Have_star, 1000)


# Tout les groupes

# le all_sprite permet de représenter tous les objet à l'écran au momment du blit  
all_sprite = pygame.sprite.Group()
# Le missile
le_missile = pygame.sprite.Group()
# Les ennemis
ennemies = pygame.sprite.Group()
# Les explosions
les_explosions = pygame.sprite.Group()
# Les étoiles
les_etoiles = pygame.sprite.Group()

class Vaisseau(pygame.sprite.Sprite):
   
    def __init__(self):
        super(Vaisseau, self).__init__()
        self.surf = pygame.image.load("images programmation/images python/spaceshift.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            if len(le_missile.sprites()) < 1:
                missile = Missile(self.rect.center)
                all_sprite.add(missile)
                le_missile.add(missile)
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            
class Missile(pygame.sprite.Sprite):
     
     def __init__(self, center_Missile):
            super(Missile, self).__init__()
            self.surf = pygame.image.load("images programmation/images python/basket-ball.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect(center = center_Missile)
    
     def update(self):
        self.rect.move_ip(15, 0)
        if self.rect.left > 800:
            self.kill()
      
class Ennemy(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Ennemy,self).__init__()
        self.surf = pygame.image.load("images programmation/images python/ennemy.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                850,
                random.randint(0, 600),
            )
        )
        self.speed = random.randint(5, 20)
        
    def update(self):
        self.rect.move_ip((-self.speed),0)
        if self.rect.right < 20:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center_vaisseau):
        super(Explosion, self).__init__()
        self._compteur = 10
        
        self.surf = pygame.image.load("images programmation/images python/collision.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(center = center_vaisseau)
       
    
    def update(self):
        self._compteur = self._compteur - 1
        if self._compteur == 0 :
            self.kill()

class Etoile(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Etoile, self).__init__()
        self.surf = pygame.image.load("images programmation/images python/étoile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (850,
            random.randint(0, 600)
            )
        )
        self.speed = random.randint(5, 10)
    
    # déplacement des étoiles de droite à gauche
    
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0 :
            self.kill()
         

# Création du vaisseau

vaisseau = Vaisseau()
all_sprite.add(vaisseau)

# Game loop

continuer = True

while continuer:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == Have_ennemy:
           new_ennemi = Ennemy()
           ennemies.add(new_ennemi)
           all_sprite.add(new_ennemi) 
        elif event.type == Have_star:
            new_star = Etoile()
            les_etoiles.add(new_star)
            all_sprite.add(new_star)       
    
    # On détermine la couleur de l'écran "ici noir"
    
    ecran.fill((0, 0, 0))
    
    # On gère la collision entre le vaisseau et l'ennemi
    
    touche_appuyee = pygame.key.get_pressed()
    if pygame.sprite.spritecollideany(vaisseau, ennemies):
        vaisseau.kill()
        explosion = Explosion(vaisseau.rect.center)
        les_explosions.add(explosion)
        all_sprite.add(explosion)
        continuer = False
    
    # On gère la collision entre le missile et l'ennemi
    
    for missile in le_missile:
        
        liste_ennemies_touches = pygame.sprite.spritecollide(missile, ennemies, True)
        if len(liste_ennemies_touches) > 0:
            missile.kill()
        for ennemi in liste_ennemies_touches:
            explosion = Explosion(ennemi.rect.center)
            les_explosions.add(explosion)
            all_sprite.add(explosion)
           
    # mise à jour des différents éléments    
    
    vaisseau.update(touche_appuyee)
    le_missile.update()
    ennemies.update()
    les_explosions.update()
    les_etoiles.update()
    
    # On fait apparaitre les groupes (Vaisseau, ennemis, explosions ,étoiles) selon les configurations respectivement définies au préalable
    
    for one_sprite in all_sprite:
       ecran.blit(one_sprite.surf, one_sprite.rect)
    
    pygame.display.flip() 
    clock.tick(80)
    
pygame.quit()   