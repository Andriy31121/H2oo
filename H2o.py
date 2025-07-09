import random

import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600


pygame.display.set_caption("Напис на екрані")
font = pygame.font.SysFont("Arial", 36)
text = font.render("H2o", True, (0, 0, 0))





class Player:
    def __init__(self, x, y, size, color, speed, name):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.color = color
        self.speed = speed
        self.name = name
        self.x = x
        self.y = y
        self.size = size
    def draw(self , window ,scale):
        draw_x = int(WIDTH // 2 - ((self.size * scale) // 2)
        draw_y = int(HEIGHT // 2 - ((self.size * scale) // 2)
        self.hitbox = pygame.Rect(draw_x , draw_y, self.size + scale , self.size + scale)
        pygame.draw.rect(window ,self.color, self.hitbox)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            pass
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.M_d]:
            self.x += self.speed
        if keys[pygame.M_s]:
            self.y += self.speed
        if keys[pygame.M_a]:
            self.x -= self.speed
        if keys[pygame.M_w]:
            self.x -= self.speed

class Food:
    def __init__(self, size, x, y, color):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.color = color
        self.x = x
        self.y = y
        self.size = size
    def draw(self , window , player_x, player_y, scale):
        draw_x = int((self.x - player_x) + WIDTH // 2)
        draw_y = int((self.y - player_y) + HEIGHT // 2)
        self.hitbox = pygame.Rect(draw_x , draw_y, self.size + scale , self.size + scale)
        pygame.draw.rect(window ,self.color, self.hitbox)




window = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

andriy = Player(WIDTH // 2, HEIGHT // 3, 50, [255, 0, 0], 3, "lubomyr")

foods = []
for i in range(300):
    food = Food(25,
                random.randint(-2000, 2000),
                random.randint(-2000, 2000),
                [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    foods.append(food)
scale = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    scale = max(0.3, min(60 / andriy.size, 1.5))

    for food in foods:
        if andriy.hitbox.colliderect(food.hitbox):
            food.x = random.randint(-2000, 2000),
            food.y = random.randint(-2000, 2000),
            andriy.size +=  2

    window.fill([123, 123, 123])
    window.blit(text, (200, 200))
    andriy.update()
    andriy.draw(window)

    for food in foods:
        food.draw(window, andriy.x, andriy.y, scale)

    pygame.display.flip()
    clock.tick(60)