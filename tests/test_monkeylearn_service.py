# import unittest
#
# from app import app
# from services.monkeylearn_service import MonkeyLearnService
#
#
# class TestMonkeyLearnService(unittest.TestCase):
#     def setUp(self):
#         app.config.from_object('config.TestingConfig')
#         self.app = app.test_client()
#
#     # Tests for function convert_mood_to_value(self, mood)
#
#     def test_it_returns_1_for_positive(self):
#         service = MonkeyLearnService('This is great and positive')
#         result = service.convert_mood_to_value('Positive')
#         self.assertEqual(1, result)
#
#     def test_it_returns_0_point_5_for_neutral(self):
#         service = MonkeyLearnService('This is so-so and neutral')
#         result = service.convert_mood_to_value('Neutral')
#         self.assertEqual(0.5, result)
#
#     def test_it_returns_0_for_negative(self):
#         service = MonkeyLearnService('This is terrible and negative')
#         result = service.convert_mood_to_value('Negative')
#         self.assertEqual(0, result)
#
#
# if __name__ == "__main__":
#     unittest.main()
