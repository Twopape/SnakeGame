import pygame
import random

class Snake():
    directions = ["right", "left", "up", "down"]
    def __init__(self):
        self.square_size = 10  # FIXME need to make adjustable
        self.rows = 50
        self.columns = 50
        self.position = [random.randint(0,self.columns-1)*self.square_size
            , random.randint(0,self.rows-1)*self.square_size]  # FIXME need to make spawn pos/direction random
        self.body = [self.position, [self.position[0] - 10, self.position[1]]]
        self.direction = self.directions[random.randint(0,3)]


    def right(self):
        if self.direction != "left":
            self.direction = "right"
    def left(self):
        if self.direction != "right":
            self.direction = "left"
    def up(self):
        if self.direction != "down":
            self.direction = "up"
    def down(self):
        if self.direction != "up":
            self.direction = "down"

    def debug(self):
        print(self.direction, self.position, self.body)

    def move(self, ate=False):
        if self.direction == "right":
            self.position[0] += 10
            if self.position[0] == 500:
                self.position[0] = 0
        if self.direction == "left":
            self.position[0] -= 10
            if self.position[0] < 0:
                self.position[0] = 490
        if self.direction == "up":
            self.position[1] -= 10
            if self.position[1] < 0:
                self.position[1] = 490
        if self.direction == "down":
            self.position[1] += 10
            if self.position[1] == 500:
                self.position[1] = 0
        x = self.position[::]
        self.body.insert(0, x)
        if not ate:
            self.body = self.body[:-1]

    def draw_on_display(self, display):

        pygame.draw.rect(display, (0, 255, 0), (self.body[0][0], self.body[0][1],
                                                self.square_size, self.square_size))

        for section in self.body[1:]:
            pygame.draw.rect(display, (255,0,0), (section[0], section[1],
                                                  self.square_size, self.square_size))

    @property
    def get_pos(self):
        return [self.body, self.position]