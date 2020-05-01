from unittest import TestCase
from snake import Snake
from unittest import mock

class test_snake(TestCase):

    def setUp(self):
        self.snake = Snake()

    def test__init__success(self):
        """010A - Test __init__ success"""
        self.assertIsNotNone(self.snake)

    def test__init__failure(self):
        """010B - Test __init__ failure"""
        with self.assertRaises(TypeError):
            self.falcon = Snake("Falcon", 100)
        with self.assertRaises(TypeError):
            self.falcon = Snake(Snake(Snake(Snake(Snake(Snake(Snake()))))))
        with self.assertRaises(TypeError):
            self.falcon = Snake(345)

    def test_right_s(self):
        """020A - Test Snake can turn right"""
        self.snake.up()
        self.snake.right()
        self.assertEqual(self.snake.debug[0],"right")

    def test_right_f(self):
        """020B - Test Snake cant turn right"""
        self.snake = Snake()
        self.snake.up()
        self.snake.left()
        self.snake.right()
        self.assertEqual(self.snake.debug[0],"left")


    def test_left_s(self):
        """030A - Test Snake can turn left"""
        self.snake.up()
        self.snake.left()
        self.assertEqual(self.snake.debug[0], "left")

    def test_left_f(self):
        """030B - Test Snake cant turn left"""
        self.snake = Snake()
        self.snake.up()
        self.snake.right()
        self.snake.left()
        self.assertEqual(self.snake.debug[0], "right")


    def test_up_s(self):
        """040A - Test Snake can turn up"""
        self.snake = Snake()
        self.snake.left()
        self.snake.up()
        self.assertEqual(self.snake.debug[0], "up")

    def test_up_f(self):
        """040B - Test Snake cant turn up"""
        self.snake = Snake()
        self.snake.left()
        self.snake.down()
        self.snake.up()
        self.assertEqual(self.snake.debug[0], "down")


    def test_down_s(self):
        """050A - Test Snake can turn down"""
        self.snake.left()
        self.snake.down()
        self.assertEqual(self.snake.debug[0], "down")

    def test_down_f(self):
        """050B - Test Snake cant turn down"""
        self.snake = Snake()
        self.snake.left()
        self.snake.up()
        self.snake.down()
        self.assertEqual(self.snake.debug[0], "up")

    def test_move(self):
        """060A - Test that snake can move"""
        self.snake.up()
        self.snake.left()
        predicted_location = [self.snake.get_pos[1][0]-10, self.snake.get_pos[1][1]]
        self.snake.move()
        self.assertEqual(self.snake.get_pos[1], predicted_location)

    def test_move_ate(self):
        """060B - Test that snake length changes after eating/is not obese)"""
        length = len(self.snake.get_pos[0])
        self.snake.move(ate=True)
        self.assertEqual(len(self.snake.get_pos[0]), length+1)

    def test_get_pos(self):
        """070A - Tests that snake spawns in a position"""
        self.assertIsNotNone(self.snake.get_pos[0])
        self.assertIsNotNone(self.snake.get_pos[1])

    @mock.patch('snake.Snake.draw_on_display')
    def test_draw_on_display(self, mock_draw_func):
        """080A - test Snake is drawn on display"""
        self.snake.draw_on_display()
        self.assertTrue(mock_draw_func.called)
