import pygame
WIDTH = 1000
HEIGHT = 600
class Player:
    def __init__(self, x, y, size, color, speed, name ):
        self.hitbox = pygame.Rect(x , y, size, size)
        self.color = color
        self.speed = speed
        self.name = name
        self.x = x
        self.y = y

        def draw(self, window):
            pygame.draw.rect(window, self.color ,self.hidht)



pygame.init()
window = pygame.display.set_mode([WIDTH, HEIGHT])

clock = pygame.time.Clock()
andriy = Player(WIDTH//2, HEIGHT//2, 50, [255, 0, 0], 0,"любомир")
foods = []
for i in range(300):
    food = Food(20,
                )
while 1==1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.fill([201, 200, 200])
    pygame.display.flip()
    clock.tick(60)