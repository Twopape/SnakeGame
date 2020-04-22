from snake import Snake
from window import Window

class Game():

    def __init__(self, playing:bool=True):
        self.playing = playing

    def play(self):
        snake = Snake()
        window = Window()
        while self.playing == True:
            window.redraw()

if __name__ == "__main__":
    game = Game()
    game.play()