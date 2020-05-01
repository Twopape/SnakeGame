from unittest import TestCase
from food import Food
from unittest import mock

class test_food(TestCase):

    def setUp(self):
        self.food = Food()

    def test__init__success(self):
        """010A - Test __init__ success"""
        self.assertIsNotNone(self.food)

    def test__init__failure(self):
        """010B - Test __init__ failure"""
        with self.assertRaises(TypeError):
            self.falcon = Food("Falcon", 100)
        with self.assertRaises(TypeError):
            self.falcon = Food(Food(Food(Food(Food(Food(Food()))))))
        with self.assertRaises(TypeError):
            self.falcon = Food(345)

    def test_get_pos(self):
        """070A - test obj spawns"""
        self.assertIsNotNone(self.food.get_pos)

    @mock.patch('food.Food.draw_on_display')
    def test_draw_on_display(self, mock_draw_func):
        """080A - test food is drawn on display"""
        self.food.draw_on_display()
        self.assertTrue(mock_draw_func.called)

    def test_new_food(self):
        """90A - test new food spawns food in a new position"""
        self.food.new_food([0,0])
        self.assertNotEqual(self.food.get_pos,[0,0])








