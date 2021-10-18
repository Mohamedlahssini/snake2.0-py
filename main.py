import pygame
from pygame.locals import *
import random

pygame.init()

#blank game window
screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake')

#game variables
cell_size = 10
direction = 1
update_snake = 0
food = [0, 0]
new_food = True
new_piece = [0, 0]
score = 0


#create snake
snake_pos = [[int(screen_width/2), int(screen_height/2)]]
snake_pos.append([int(screen_width/2), int(screen_height/2) + cell_size])
snake_pos.append([int(screen_width/2), int(screen_height/2) + cell_size * 2])
snake_pos.append([int(screen_width/2), int(screen_height/2) + cell_size * 3])

#define font
font = pygame.font.SysFont(None, 40)

#game background color
bg = (255, 200, 150)
body_inner = (50, 175, 25)
body_outer = (100, 100, 200)
red = (255, 255, 0)
blue = (0, 0, 255)
food_col = (50, 50, 20)

def drawscreen():
    screen.fill(bg)

def draw_score():
	score_txt = 'Score: ' + str(score)
	score_img = font.render(score_txt, True, blue)
	screen.blit(score_img, (0, 0))

run = True

while run:
    drawscreen()
    draw_score()

    #iterate through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4

    #create food
    if new_food == True:
        new_food = False
        food[0] = cell_size * random.randint(0, (screen_width / cell_size) - 1)
        food[1] = cell_size * random.randint(0, (screen_height / cell_size) - 1)

    #draw food
    pygame.draw.rect(screen, food_col, (food[0], food[1], cell_size, cell_size))

    # check if food has been eaten
    if snake_pos[0] == food:
        new_food = True
        # create a new piece at the last point of the snake's tail
        new_piece = list(snake_pos[-1])
        # add an extra piece to the snake
        if direction == 1:
            new_piece[1] += cell_size
        # heading down
        if direction == 3:
            new_piece[1] -= cell_size
        # heading right
        if direction == 2:
            new_piece[0] -= cell_size
        # heading left
        if direction == 4:
            new_piece[0] += cell_size

        # attach new piece to the end of the snake
        snake_pos.append(new_piece)

        # increase score
        score += 1


    if update_snake > 99:
        update_snake = 0
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        #heading up
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 2:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] + cell_size
        if direction == 4:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] - cell_size


    #draw snake
    head = 1
    #snake head color
    for x in snake_pos:
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_outer, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, red, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
            head = 0

    pygame.display.update()
    update_snake += 1

pygame.quit()