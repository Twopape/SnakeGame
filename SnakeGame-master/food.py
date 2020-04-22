import pygame
import random


class Food():
    def __init__(self):
        self.food_position = [] # xy coords for food
        self.square_size = 10  # FIXME need to make adjustable
        self.rows = 50
        self.columns = 50

    def new_food(self, snake_pos):
        new_pos = [random.randint(0,self.columns)*self.square_size
            , random.randint(0,self.rows)*self.square_size]
        while any(new_pos == body for body in snake_pos):
            new_pos = [random.randint(0, self.columns) * self.square_size
                , random.randint(0, self.rows) * self.square_size]
        self.food_position = new_pos

    def draw_on_display(self, display):
        pygame.draw.rect(display, (0, 0, 255), (self.food_position[0], self.food_position[1],
                         self.square_size, self.square_size))

    @property
    def get_pos(self):
        return self.food_position
