from snake import Snake
from food import Food
import pygame


# initalizes objects/game
pygame.init() #creates game
pygame.font.init() # gets pygame fonts
snake = Snake() # creates snake
clock = pygame.time.Clock() #fps setter
food = Food() #creats food

DISPLAY = pygame.display.set_mode((500, 500))  # FIXME make window size adjustable
pygame.display.set_caption('Snake Game')

# Temporary window:  fifty 10 by 10 squares


# TEXT FONTS
menu_buttons = pygame.font.SysFont("comicsansms",20)

# Sound Files
lose_sound = pygame.mixer.Sound("sound/game_loss.wav")
food_collect_sound = pygame.mixer.Sound("sound/food_collect.wav")
hee_heed = False
# Image Files
michael_img = pygame.image.load("images/michael.png")
game = True

food.new_food(snake.get_pos[0]) #spawns food at a random location not on snake


# Global Variables
screen = "menu"

def button(msg,x,y,w,h,color,click_color,text_color, font, action=None):
    mouse = pygame.mouse.get_pos()
    print(mouse)
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        button = pygame.draw.rect(DISPLAY, click_color,(x,y,w,h))
        if click[0] == 1 and action != None:
            return action()
    else:
        button = pygame.draw.rect(DISPLAY,color,(x,y,w,h))
    text = font.render(msg,True,text_color)
    text_rect = text.get_rect()
    text_rect.center = (x+w//2,y+h//2)
    DISPLAY.blit(text, text_rect)





def sample_action():
    return "game"

def check_for_death():
    snake.debug()
    if any(snake.get_pos[1] == part for part in snake.get_pos[0][1:]):
        # check if head is on body part this frame

        return True
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
                screen = "menu"
                snake = Snake()
                food.new_food(snake.get_pos[0])

        if not hee_heed: # hee hee is the loss sound
            pygame.mixer.Sound.play(lose_sound)
            hee_heed = True
        DISPLAY.fill([255, 0, 0])
        DISPLAY.blit(michael_img, (100, 100))
        pygame.display.flip()


    elif screen == "menu":
        DISPLAY.fill([0, 0, 0])
        response = button("hell",150,150,50,50,[255,255,0],[255,0,0],[255,0,255],menu_buttons, sample_action)
        if response == "game": # simple menu system
            screen = "game"
        pygame.display.flip()

        # idk why but with out the code at the bottom, it crashes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


    clock.tick(200) #FIXME we need to have different clock timers for the menu and the game or snake too speed or button lags
    print(screen)
    print("refreshed")