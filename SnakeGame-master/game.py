from snake import Snake
from food import Food
import pygame
import tkinter as tk
from tkinter import simpledialog, messagebox
from os import path, remove
import requests


class Game():
    def __init__(self):
        self.ROOT = tk.Tk()
        self.ROOT.withdraw()

        # initalizes objects/game
        pygame.init()  # creates game
        pygame.font.init()  # gets pygame fonts
        self.snake = Snake()  # creates snake
        self.clock = pygame.time.Clock()  # fps setter
        self.food = Food()  # creates food
        self.scores = dict()

        self.DISPLAY = pygame.display.set_mode((500, 500))  # FIXME make window size adjustable
        pygame.display.set_caption('Snake Game')

        # Temporary window:  fifty 10 by 10 squares

        # TEXT FONTS
        self.menu_buttons = pygame.font.SysFont("comicsansms", 20)

        # Sound Files
        self.lose_sound = pygame.mixer.Sound("sound/game_loss.wav")
        self.food_collect_sound = pygame.mixer.Sound("sound/food_collect.wav")
        self.hee_heed = False
        # Image Files
        self.michael_img = pygame.image.load("images/michael.png")
        self.game = True

        self.food.new_food(self.snake.get_pos[0])  # spawns food at a random location not on snake

        # Global Variables
        self.screen = "menu"
        self.restart = True
        self.target_url = "http://localhost:1337"
        self.difficulty = ""
        self.score = 0
        self.hunger = 0  # time since last meal

    def upload(self):

        if path.exists("db.txt"):  # FIXME
            file = open("db.txt", "r")
            csvlist = file.readlines()
            print(csvlist)
            if csvlist != []:
                for person in csvlist[:-1]:
                    data = {}
                    data["player"] = person.split(",")[0]
                    data["score"] = int("".join(list(person.split(",")[1])[:-1]))
                    data["difficulty"] = person.split(",")[2].capitalize()
                    response = requests.post(self.target_url + "/Player/AddScore", data=data)
                    print(response)
                data = {}
                data["player"] = csvlist[-1].split(",")[0]
                data["score"] = int(csvlist[-1].split(",")[1])
                data["difficulty"] = self.difficulty.capitalize()
                response = requests.post(self.target_url + "/Player/AddScore", data=data)
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

    def button(self, msg, x, y, w, h, color, click_color, text_color, font, action=None):
        mouse = pygame.mouse.get_pos()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.DISPLAY, click_color, (x, y, w, h))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return action()
        else:
            pygame.draw.rect(self.DISPLAY, color, (x, y, w, h))
        text = font.render(msg, True, text_color)
        text_rect = text.get_rect()
        text_rect.center = (x + w // 2, y + h // 2)
        self.DISPLAY.blit(text, text_rect)

    def record_score(self, name, score):
        if path.exists("db.txt"):
            file = open("db.txt", "r")
            csvlist = file.readlines()

            for line in csvlist:
                item = line.split(",")
                self.scores[item[0]] = item[1]
            if name in self.scores:
                if int(self.scores[name]) >= int(score):
                    file.close()
                    return False
                else:
                    file.close()
                    self.scores[name] = self.score
                    file = open("db.txt", "w")
                    for key in self.scores:
                        file.write(f"\n{key},{int(self.scores[key])},{self.difficulty}")
                    csvlist.pop(0)
                    file.close()
                    return True
            else:
                file.close()
                file = open("db.txt", "a")
                file.write(f"\n{name},{int(score)},{self.difficulty}")
                file.close()
                return True
        else:
            file = open("db.txt", "w")
            file.write(f"{name},{int(score)},{self.difficulty}")
            file.close()
            return True

    def menu_action(self):
        self.screen = "menu"

    def record_action(self):

        name = simpledialog.askstring(title="Test",
                                      prompt="What's your Name?:")
        if name is not None:
            if name != '':
                try:
                    int(name)
                    messagebox.showinfo("Invalid.", "The name you entered is invalid.")
                except ValueError:
                    if self.record_score(name, self.score):
                        messagebox.showinfo("Success", f"Score of {int(self.score)} recorded for player {name}!")
                        self.screen = "menu"
                        return "success"
                    else:
                        messagebox.showinfo("Failure", f"{name} already has a higher score than {int(self.score)}.")
            else:

                messagebox.showinfo("Invalid.", "The name you entered is invalid.")
        return "menu"

    def calculate_score(self, ate=False):

        multiplier = 0
        if self.difficulty == "easy":
            multiplier = 5
        elif self.difficulty == "medium":
            multiplier = 7.5
        elif self.difficulty == "hard":
            multiplier = 10
        if not ate:
            self.hunger += 1
            self.score = self.score - self.hunger
        else:
            self.hunger = 0
            self.score = self.score + 1000 * multiplier * (len(self.snake.get_pos[0]) / 10 + 1)

        if self.score <= 0:
            self.score = 0

    def easy_action(self):

        self.food = Food()
        self.snake = Snake()
        self.DISPLAY.fill([0, 0, 0])
        self.food.new_food(self.snake.get_pos[0])
        self.snake.draw_on_display(self.DISPLAY)
        self.food.draw_on_display(self.DISPLAY)
        self.difficulty = "easy"
        self.screen = "game"

    def medium_action(self):
        self.food = Food()
        self.snake = Snake()
        self.DISPLAY.fill([0, 0, 0])
        self.food.new_food(self.snake.get_pos[0])
        self.snake.draw_on_display(self.DISPLAY)
        self.food.draw_on_display(self.DISPLAY)
        self.difficulty = "medium"
        self.screen = "game"

    def hard_action(self):
        self.food = Food()
        self.snake = Snake()
        self.DISPLAY.fill([0, 0, 0])
        self.food.new_food(self.snake.get_pos[0])
        self.snake.draw_on_display(self.DISPLAY)
        self.food.draw_on_display(self.DISPLAY)
        self.difficulty = "hard"
        self.screen = "game"

    def check_for_death(self):
        if any(self.snake.get_pos[1] == part for part in self.snake.get_pos[0][1:]):
            # check if head is on body part this frame

            return True
        return False

    def play(self):
        while self.game is True:

            if self.screen == "game":

                for event in pygame.event.get():  # Arrow key inputs
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.snake.left()
                        if event.key == pygame.K_RIGHT:
                            self.snake.right()
                        if event.key == pygame.K_UP:
                            self.snake.up()
                        if event.key == pygame.K_DOWN:
                            self.snake.down()

                # snake.debug() #debug info
                if self.check_for_death():  # snake will die next round
                    self.screen = "lose"

                if self.snake.get_pos[1] == self.food.get_pos:
                    # pygame.mixer.Sound.play(food_collect_sound)
                    self.snake.move(ate=True)  # makes snake longer if snake on food
                    self.calculate_score(ate=True)
                    self.food.new_food(self.snake.get_pos[0])
                else:
                    self.calculate_score()
                    self.snake.move()

                self.DISPLAY.fill([0, 0, 0])

                self.button(str(int(self.score)), 250, 0, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], self.menu_buttons)
                self.snake.draw_on_display(self.DISPLAY)
                self.food.draw_on_display(self.DISPLAY)
                pygame.display.flip()



            elif self.screen == "lose":
                self.DISPLAY.fill([0, 0, 0])
                if not self.hee_heed:  # hee hee is the loss sound
                    # pygame.mixer.Sound.play(lose_sound)
                    self.hee_heed = True
                self.button("Play!", 150, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], self.menu_buttons,
                            self.menu_action)
                self.button("Record score!", 250, 250, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255], self.menu_buttons,
                            self.record_action)
                self.button(f"Score: {int(self.score)}", 200, 200, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255],
                            self.menu_buttons)
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()



            elif self.screen == "menu":
                self.score = 0
                self.DISPLAY.fill([0, 0, 0])
                response = self.button("EASY!", 150, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255],
                                       self.menu_buttons, self.easy_action)
                response2 = self.button("MEDIUM!", 235, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255],
                                        self.menu_buttons, self.medium_action)
                response3 = self.button("HARD!", 350, 150, 50, 50, [0, 0, 0], [0, 0, 0], [255, 0, 255],
                                        self.menu_buttons, self.hard_action)
                if path.exists("db.txt"):
                    self.button("Upload Scores", 150, 250, 50, 50, [100, 0, 0], [200, 0, 0], [255, 0, 255],
                                self.menu_buttons,
                                self.upload)
                if response == "game":  # simple menu system
                    self.screen = "game"
                pygame.display.flip()

                # idk why but with out the code at the bottom, it crashes
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

            if self.screen != "game":
                self.clock.tick(200)
            else:
                if self.difficulty == "easy":
                    self.clock.tick(10)
                elif self.difficulty == "medium":
                    self.clock.tick(15)
                elif self.difficulty == "hard":
                    self.clock.tick(20)
                else:
                    self.clock.tick(1)


if __name__ == "__main__":
    game = Game()
    game.play()
