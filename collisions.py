import sys, pygame

pygame.init()
clock = pygame.time.Clock()
size = screen_width, screen_height = 1080, 720
white = 255, 255, 255
black = 0, 0, 0
screen = pygame.display.set_mode(size)


class Square:

    def __init__(self, x, y, width, height, speed: list):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    def get_values(self):
        return [self.x, self.y, self.width, self.height]

    def accelerate(self, speed):
        self.x += speed[0]
        self.y += speed[1]

    def only_in_screen(self):
        if self.x < 0 or self.x+self.width > screen_width:
            self.speed[0] = -self.speed[0]
        if self.y < 0 or self.y +self.height > screen_height:
            self.speed[1] = -self.speed[1]


# Square 1
square_1 = Square(75, 75, 100, 100, [2, 3])

# Square 2
square_2 = Square(690, 500, 150, 150, [4, 8])


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    square_1.only_in_screen()
    square_2.only_in_screen()
    square_1.accelerate(speed=square_1.speed)
    square_2.accelerate(speed=square_2.speed)

    screen.fill(white)
    pygame.draw.rect(screen, black, rect=square_1.get_values())
    pygame.draw.rect(screen, black, rect=square_2.get_values())
    pygame.display.flip()
