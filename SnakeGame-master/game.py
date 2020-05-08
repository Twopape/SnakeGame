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


def upload():
    global screen

    if path.exists("db.txt"): # FIXME
        file = open("db.txt", "r")
        csvlist = file.readlines()
        print(csvlist)
        for person in csvlist[:-1]:
            data = {}
            data["player"] = person.split(",")[0]
            data["score"] = "".join(list(person.split(",")[1])[:-1])
            data["difficulty"] = "MJ"
            response = requests.post(target_url + "/Player/AddScore", data=data)
            print(data, response)
        data = {}
        data["player"] = csvlist[-1].split(",")[0]
        data["score"] = csvlist[-1].split(",")[1]
        data["difficulty"] = "MJ"
        response = requests.post(target_url + "/Player/AddScore", data=data)
        print(data, response)
        messagebox.showinfo("Success!", f"Scores have been uploaded")
        file.close()
        remove("db.txt")
    else:
        messagebox.showinfo("FAILURE!", f"No new Scores")



def button(msg, x, y, w, h, color, click_color, text_color, font, action=None):
    mouse = pygame.mouse.get_pos()
    print(mouse)
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        button = pygame.draw.rect(DISPLAY, click_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            return action()
    else:
        button = pygame.draw.rect(DISPLAY, color, (x, y, w, h))
    text = font.render(msg, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (x + w // 2, y + h // 2)
    DISPLAY.blit(text, text_rect)


def record_score(name, score):
    if path.exists("db.txt"):
        file = open("db.txt", "r")
        csvlist = file.readlines()
        csvlist.pop(0)
        for line in csvlist:
            item = line.split(",")
            scores[item[0]] = item[1]
        if name in scores:
            if int(scores[name]) >= score:
                file.close()
                return False
            else:
                file.close()
                scores[name] = score
                file = open("db.txt", "w")
                for key in scores:
                    file.write(f"\n{key},{scores[key]}")
                file.close()
                return True
        else:
            file.close()
            file = open("db.txt", "a")
            file.write(f"\n{name},{score}")
            file.close()
            return True
    else:
        file = open("db.txt", "w")
        file.write(f"{name},{score}")
        file.close()
        return True


def menu_action():
    return "menu"


def record_action():
    global screen

    score = len(snake.get_pos[0]) - 1
    name = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")
    if name is not None:
        if name != '':
            try:
                int(name)
                messagebox.showinfo("Invalid.", "The name you entered is invalid.")
            except ValueError:
                if record_score(name, score):
                    messagebox.showinfo("Success", f"Score of {score} recorded for player {name}!")
                    screen = "menu"
                    return "success"
                else:
                    messagebox.showinfo("Failure", f"{name} already has a higher score than {score}.")
        else:

            messagebox.showinfo("Invalid.", "The name you entered is invalid.")
    return "menu"


def game_action():
    global screen
    global food
    global snake

    food = Food()
    snake = Snake()
    DISPLAY.fill([0, 0, 0])
    food.new_food(snake.get_pos[0])
    snake.draw_on_display(DISPLAY)
    food.draw_on_display(DISPLAY)
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
            print("snake death")
            screen = "lose"

        if snake.get_pos[1] == food.get_pos:
            # pygame.mixer.Sound.play(food_collect_sound)
            snake.move(ate=True)  # makes snake longer if snake on food
            food.new_food(snake.get_pos[0])
        else:
            snake.move()

        DISPLAY.fill([0, 0, 0])
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
        button(f"Score: {len(snake.get_pos[0]) - 1}", 200, 200, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255],
                           menu_buttons)
        button("Upload Scores", 150, 250, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], menu_buttons,
               upload)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



    elif screen == "menu":
        DISPLAY.fill([0, 0, 0])
        response = button("Play!", 150, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], menu_buttons, game_action)
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

    clock.tick(15)  # FIXME we need to have different clock timers for the menu and the game or snake too speed or button lags
    print(screen)
    print("refreshed")
