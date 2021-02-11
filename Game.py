import pygame, sys
from Player import Player
from Fruits import Fruits

class Game:

    def __init__(self):
        #define if the game is started or not 
        self.is_playing = False
        # generate a player 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.score = 0
        self.highest_score = [0]
        #generate fruits
        self.all_fruits = pygame.sprite.Group()
        self.pressed = {}
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def start(self):
        self.is_playing = True
        for i in range(5):
            self.spawn_fruit()

    def game_over(self):
        self.all_fruits = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        print("Game Over !")
        self.highScore(self.score)

    def update(self, screen):
        Police = pygame.font.Font("Fonts/bold_game_font_7.ttf", 40)
        Rendu = Police.render(f"Score : {self.score}", 1, (255,255,255)) 
        screen.blit(Rendu, (10, 40))

    def spawn_fruit(self):
        fruit = Fruits(self)
        self.all_fruits.add(fruit)

    def highScore(self, score):
        for i in self.highest_score:
            if score > i:
                self.highest_score.insert(0,score)
                break
       