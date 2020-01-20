import unittest
import json
from unittest.mock import patch
from app import app
from services.watson_service import WatsonService


class TestWatsonService(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()


    @patch.object(WatsonService, 'get_watson_text_analyze')
    def test_watson_service_happy_path(self, mock_text_sentiment):
        file_path = 'tests/fixtures/watson_positive.json'
        with open(file_path) as json_file:
            ml_data = json.load(json_file)

        mock_text_sentiment.return_value = ml_data

        service = WatsonService('Super positive great happy fun times awesome exciting')
        result = service.get_sentiment_value()

        self.assertEqual( 1, result)


    @patch.object(WatsonService, 'get_watson_text_analyze')
    def test_watson_service_sad_pathes(self, mock_text_sentiment):
        file_path = 'tests/fixtures/watson_positive.json'
        with open(file_path) as json_file:
            ml_data = json.load(json_file)

        mock_text_sentiment.return_value = ml_data

        #Not enough characters for sentiment analysis
        service = WatsonService('Super positive')
        result = service.get_sentiment_value()

        self.assertEqual( 0.5, result)

        #No characters
        service = WatsonService('')
        result = service.get_sentiment_value()

        self.assertEqual( 0.5, result)


if __name__ == "__main__":
    unittest.main()
