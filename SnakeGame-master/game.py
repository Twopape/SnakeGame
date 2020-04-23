from snake import Snake
from food import Food
import pygame


# initalizes objects/game
pygame.init()

DISPLAY = pygame.display.set_mode((500, 500))  # FIXME make window size adjustable
DISPLAY.fill([0,0,0])
# Temporary window:  fifty 10 by 10 squares

# Sound Files
lose_sound = pygame.mixer.Sound("sound/game_loss.wav")
food_collect_sound = pygame.mixer.Sound("sound/food_collect.wav")
hee_heed = False
# Image Files
michael_img = pygame.image.load("images/michael.png")
game = True
snake = Snake()
clock = pygame.time.Clock()
food = Food()
food.new_food(snake.get_pos[0]) #spawns food at a random location not on snake


# Global Variables
screen = "game"




def check_for_death():
    snake.debug()
    if any(snake.get_pos[1] == part for part in snake.get_pos[0][1:]):
        # check if head is GOING to be
        return True                                                     # on a body part next frame
    return False

while game is True:

    if screen == "game":
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
        if check_for_death():  # snake will die next round
            print("snake death")
            screen = "lose"

        if snake.get_pos[1] == food.get_pos:
            pygame.mixer.Sound.play(food_collect_sound)
            snake.move(ate=True) # makes snake longer if snake on food
            food.new_food(snake.get_pos[0])
        else:
            snake.move()

        DISPLAY.fill([0,0,0])
        snake.draw_on_display(DISPLAY)
        food.draw_on_display(DISPLAY)
        pygame.display.flip()



    elif screen == "lose":
        for event in pygame.event.get(): # Arrow key inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen = "game"
                snake = Snake()
                food.new_food(snake.get_pos[0])

        if not hee_heed:
            pygame.mixer.Sound.play(lose_sound)
            hee_heed = True
        DISPLAY.fill([255, 0, 0])
        DISPLAY.blit(michael_img, (100, 100))


        pygame.display.flip()

    clock.tick(5)
    print(screen)
    print("refreshed")