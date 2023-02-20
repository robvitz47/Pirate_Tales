import pygame
import random

# initialize pygame
pygame.init()

# set up the game window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fighting Game")

# set up the clock
clock = pygame.time.Clock()

# set up the player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT // 2

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
        elif keys[pygame.K_UP]:
            self.rect.y -= 5
        elif keys[pygame.K_DOWN]:
            self.rect.y += 5

# set up the enemy sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 100
        self.rect.y = HEIGHT // 2

    def update(self):
        # randomly move the enemy
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        self.rect.x += dx
        self.rect.y += dy

# set up the ground sprite
class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/ground.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# set up the sprites group
sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()
sprites.add(player, enemy)

# set up the ground tiles
ground_tiles = pygame.sprite.Group()
for i in range(0, WIDTH, 50):
    ground = Ground(i, HEIGHT-50)
    ground_tiles.add(ground)

# set up collision detection
def detect_collision(sprite1, sprite2):
    return pygame.sprite.collide_rect(sprite1, sprite2)

# set up the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the player sprite
    keys = pygame.key.get_pressed()
    player.update(keys)

    # update the enemy sprite
    enemy.update()

    # check for collisions
    if detect_collision(player, enemy):
        print("Collision detected!")

    # draw the sprites
    win.fill((255, 255, 255))
    ground_tiles.draw(win)
    sprites.draw(win)

    # update the display
    pygame.display.update()

    # set the game clock
    clock.tick(60)

# quit the game
pygame.quit()
