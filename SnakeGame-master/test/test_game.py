from unittest import TestCase
from game import Game
from unittest import mock
from os import path
class test_game(TestCase):

    def setUp(self):
        self.game = Game()

    def test_easy_action(self):
        self.game.easy_action()
        self.assertEqual(self.game.difficulty, "easy")
    def test_medium_action(self):
        self.game.medium_action()
        self.assertEqual(self.game.difficulty, "medium")
    def test_hard_action(self):
        self.game.hard_action()
        self.assertEqual(self.game.difficulty, "hard")

    @mock.patch('game.Game.play')
    def test_game_loop(self, mock_play):
        self.game.screen = "menu"
        self.game.play()
        self.assertTrue(mock_play.called)

        self.game.screen = "lose"
        self.game.play()
        self.assertTrue(mock_play.called)

        self.game.screen = "game"
        self.game.play()
        self.assertTrue(mock_play.called)

    @mock.patch('game.Game.upload')
    def test_upload(self, mock_upload):
        self.game.upload()
        self.assertTrue(mock_upload.called)

    @mock.patch('game.Game.record_score')
    def test_record_score(self, mock_record_score):
        self.game.record_score("tester",123)
        self.assertTrue(mock_record_score.called)

    @mock.patch('game.Game.button')
    def test_button(self,mock_button):
        def test():
            pass
        self.game.button("tester", 123,123,123,123,[3,4,4],[3,4,4],[3,4,4],None)
        self.assertTrue(mock_button.called)

        self.game.button("tester", 123,123,123,123,[3,4,4],[3,4,4],[3,4,4],None, test())
        self.assertTrue(mock_button.called)

    def test_menu_action(self):
        self.game.menu_action()
        self.assertEqual(self.game.screen,"menu")

    @mock.patch('game.Game.record_action')
    def test_record_action(self, mock_record_action):
        self.game.record_action()
        self.assertTrue(mock_record_action.called)

    @mock.patch('game.Game.check_for_death')
    def test_check_for_death(self, mock_check_for_death):
        self.game.check_for_death()
        self.assertTrue(mock_check_for_death.called)


