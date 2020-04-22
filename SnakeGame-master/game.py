from snake import Snake
from food import Food
import pygame


# initalizes objects/game
pygame.init()

DISPLAY = pygame.display.set_mode((500, 500))  # FIXME make window size adjustable
DISPLAY.fill([255,255,255])
# Temporary window:  fifty 10 by 10 squares


playing = True
snake = Snake()
clock = pygame.time.Clock()
food = Food()
food.new_food(snake.get_pos[0]) #spawns food at a random location not on snake

while playing is True:

    for event in pygame.event.get(): # Arrow key inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.left()
            if event.key == pygame.K_RIGHT:
                snake.right()
            if event.key == pygame.K_UP:
                snake.up()
            if event.key == pygame.K_DOWN:
                snake.down()

    #snake.debug() #debug info
    if snake.get_pos[1] == food.get_pos:
        snake.move(ate=True)
        food.new_food(snake.get_pos[0])
    else:
        snake.move()
    DISPLAY.fill([255, 255, 255])
    snake.draw_on_display(DISPLAY)
    food.draw_on_display(DISPLAY)
    pygame.display.flip()
    clock.tick(5)
    print("refreshed")
