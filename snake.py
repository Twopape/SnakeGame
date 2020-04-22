import pygame

class Snake():
    def __init__(self, position:tuple=(10,10)):
        self.position = position
        self.body = []