import pygame

# FIXME need to prevent snake from leaving screen
class Snake():
    def __init__(self):
        self.position = [100,50]  # FIXME need to make spawn pos/direction random
        self.body = [[100,50],[90,50],[80,50],[70,50],[60,50]]
        self.direction = "right"
        self.square_size = 10  # FIXME need to make adjustable
        self.rows = 50
        self.columns = 50

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
        print(self.direction, self.position,self.body)

    def move(self, ate=False):
        if self.direction == "right":
            self.position[0] += 10
        if self.direction == "left":
            self.position[0] -= 10
        if self.direction == "up":
            self.position[1] -= 10
        if self.direction == "down":
            self.position[1] += 10
        x = self.position[::]
        self.body.insert(0, x)
        if not ate:
            self.body = self.body[:-1]

    def draw_on_display(self, display):

        for section in self.body[1:]:
            pygame.draw.rect(display, (255,0,0), (section[0], section[1],
                                                  self.square_size, self.square_size))
        pygame.draw.rect(display, (0, 255, 0), (self.body[0][0], self.body[0][1],
                                                self.square_size, self.square_size))

    @property
    def get_pos(self):
        return [self.body, self.position]
