import sys, pygame

pygame.init()
size = width, height = 1440, 1080
white = 255, 255, 255
black = 0, 0, 0
screen = pygame.display.set_mode(size)

# Square 1
speed_1 = [2, 3]
side_1 = 100
x_1 = side_1 / 2 - 25
y_1 = side_1 / 2 - 25  # Coordinates of the center of the square
square_1 = [x_1, y_1, side_1, side_1, speed_1]

# Square 2

speed_2 = [4, -5]
side_2 = 150
x_2 = (width / 2) - (side_2 / 2)
y_2 = (height / 3) + (side_2 / 2)  # Coordinates of the center of the square
square_2 = [x_2, y_2, side_2, side_2, speed_2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(white)
    pygame.draw.rect(screen, black, rect=square_1[0:4])
    pygame.draw.rect(screen, black, rect=square_2[0:4])
    pygame.display.flip()
