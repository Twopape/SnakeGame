from snake import Snake
from food import Food
import pygame
import tkinter as tk
from tkinter import simpledialog, messagebox
from os import path, remove
import requests

ROOT = tk.Tk()
ROOT.withdraw()

# initalizes objects/game
pygame.init()  # creates game
pygame.font.init()  # gets pygame fonts
snake = Snake()  # creates snake
clock = pygame.time.Clock()  # fps setter
food = Food()  # creats food
scores = dict()

DISPLAY = pygame.display.set_mode((500, 500))  # FIXME make window size adjustable
pygame.display.set_caption('Snake Game')

# Temporary window:  fifty 10 by 10 squares


# TEXT FONTS
menu_buttons = pygame.font.SysFont("comicsansms", 20)

# Sound Files
lose_sound = pygame.mixer.Sound("sound/game_loss.wav")
food_collect_sound = pygame.mixer.Sound("sound/food_collect.wav")
hee_heed = False
# Image Files
michael_img = pygame.image.load("images/michael.png")
game = True

food.new_food(snake.get_pos[0])  # spawns food at a random location not on snake

# Global Variables
screen = "menu"
restart = True
target_url = "http://localhost:1337"
difficulty = ""
score = 0
hunger = 0 # time since last meal

def upload():
    global screen

    if path.exists("db.txt"): # FIXME
        file = open("db.txt", "r")
        csvlist = file.readlines()
        print(csvlist)
        if csvlist != []:
            for person in csvlist[:-1]:
                data = {}
                data["player"] = person.split(",")[0]
                data["score"] = int("".join(list(person.split(",")[1])[:-1]))
                data["difficulty"] = person.split(",")[2].capitalize()
                response = requests.post(target_url + "/Player/AddScore", data=data)
                print(response)
            data = {}
            data["player"] = csvlist[-1].split(",")[0]
            data["score"] = int(csvlist[-1].split(",")[1])
            data["difficulty"] = difficulty.capitalize()
            response = requests.post(target_url + "/Player/AddScore", data=data)
            print(response)
            messagebox.showinfo("Success!", f"Scores have been uploaded")
            file.close()
            remove("db.txt")
        else:
            messagebox.showinfo("FAILURE!", f"No new Scores")
            return ""
    else:
        messagebox.showinfo("FAILURE!", f"No new Scores")
        return ""



def button(msg, x, y, w, h, color, click_color, text_color, font, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAY, click_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            return action()
    else:
        pygame.draw.rect(DISPLAY, color, (x, y, w, h))
    text = font.render(msg, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (x + w // 2, y + h // 2)
    DISPLAY.blit(text, text_rect)


def record_score(name, score):
    if path.exists("db.txt"):
        file = open("db.txt", "r")
        csvlist = file.readlines()

        for line in csvlist:
            item = line.split(",")
            scores[item[0]] = item[1]
        if name in scores:
            if int(scores[name]) >= int(score):
                file.close()
                return False
            else:
                file.close()
                scores[name] = score
                file = open("db.txt", "w")
                for key in scores:
                    file.write(f"\n{key},{int(scores[key])},{difficulty}")
                csvlist.pop(0)
                file.close()
                return True
        else:
            file.close()
            file = open("db.txt", "a")
            file.write(f"\n{name},{int(score)},{difficulty}")
            file.close()
            return True
    else:
        file = open("db.txt", "w")
        file.write(f"{name},{int(score)},{difficulty}")
        file.close()
        return True


def menu_action():
    global screen
    screen = "menu"


def record_action():
    global screen
    global score

    name = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")
    if name is not None:
        if name != '':
            try:
                int(name)
                messagebox.showinfo("Invalid.", "The name you entered is invalid.")
            except ValueError:
                if record_score(name, score):
                    messagebox.showinfo("Success", f"Score of {int(score)} recorded for player {name}!")
                    screen = "menu"
                    return "success"
                else:
                    messagebox.showinfo("Failure", f"{name} already has a higher score than {int(score)}.")
        else:

            messagebox.showinfo("Invalid.", "The name you entered is invalid.")
    return "menu"

def calculate_score(ate=False):
    global score
    global hunger

    multiplier = 0
    if difficulty == "easy":
        multiplier = 5
    elif difficulty == "medium":
        multiplier = 7.5
    elif difficulty == "hard":
        multiplier = 10
    if ate == False:
        hunger += 1
        score = score - hunger
    else:
        hunger = 0
        score = score + 1000*multiplier*(len(snake.get_pos[0])/10+1)

    if score <= 0:
        score = 0




def easy_action():
    global screen
    global food
    global snake
    global difficulty

    food = Food()
    snake = Snake()
    DISPLAY.fill([0, 0, 0])
    food.new_food(snake.get_pos[0])
    snake.draw_on_display(DISPLAY)
    food.draw_on_display(DISPLAY)
    difficulty = "easy"
    screen = "game"

def medium_action():
    global screen
    global food
    global snake
    global difficulty

    food = Food()
    snake = Snake()
    DISPLAY.fill([0, 0, 0])
    food.new_food(snake.get_pos[0])
    snake.draw_on_display(DISPLAY)
    food.draw_on_display(DISPLAY)
    difficulty = "medium"
    screen = "game"

def hard_action():
    global screen
    global food
    global snake
    global difficulty

    food = Food()
    snake = Snake()
    DISPLAY.fill([0, 0, 0])
    food.new_food(snake.get_pos[0])
    snake.draw_on_display(DISPLAY)
    food.draw_on_display(DISPLAY)
    difficulty = "hard"
    screen = "game"


def check_for_death():
    if any(snake.get_pos[1] == part for part in snake.get_pos[0][1:]):
        # check if head is on body part this frame

        return True
    return False


while game is True:


    if screen == "game":


        for event in pygame.event.get():  # Arrow key inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.left()
                if event.key == pygame.K_RIGHT:
                    snake.right()
                if event.key == pygame.K_UP:
                    snake.up()
                if event.key == pygame.K_DOWN:
                    snake.down()

        # snake.debug() #debug info
        if check_for_death():  # snake will die next round
            screen = "lose"

        if snake.get_pos[1] == food.get_pos:
            # pygame.mixer.Sound.play(food_collect_sound)
            snake.move(ate=True)  # makes snake longer if snake on food
            calculate_score(ate=True)
            food.new_food(snake.get_pos[0])
        else:
            calculate_score()
            snake.move()

        DISPLAY.fill([0, 0, 0])

        button(str(int(score)), 250, 0, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], menu_buttons)
        snake.draw_on_display(DISPLAY)
        food.draw_on_display(DISPLAY)
        pygame.display.flip()



    elif screen == "lose":
        DISPLAY.fill([0, 0, 0])
        if not hee_heed:  # hee hee is the loss sound
            # pygame.mixer.Sound.play(lose_sound)
            hee_heed = True
        button("Play!", 150, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], menu_buttons,
                          menu_action)
        button("Record score!", 250, 250, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], menu_buttons,
                           record_action)
        button(f"Score: {int(score)}", 200, 200, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255],
                           menu_buttons)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



    elif screen == "menu":
        score = 0
        DISPLAY.fill([0, 0, 0])
        response = button("EASY!", 150, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], menu_buttons, easy_action)
        response2 = button("MEDIUM!", 235, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], menu_buttons, medium_action)
        response3 = button("HARD!", 350, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], menu_buttons, hard_action)
        if path.exists("db.txt"):
            button("Upload Scores", 150, 250, 50, 50, [100, 0, 0], [200, 0, 0], [255, 0, 255], menu_buttons,
                   upload)
        if response == "game":  # simple menu system
            screen = "game"
        pygame.display.flip()

        # idk why but with out the code at the bottom, it crashes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    if screen != "game":
        clock.tick(200)  # FIXME we need to have different clock timers for the menu and the game or snake too speed or button lags
    else:
        if difficulty == "easy":
            clock.tick(10)
        elif difficulty == "medium":
            clock.tick(15)
        elif difficulty == "hard":
            clock.tick(20)
        else:
            clock.tick(1)

