import unittest
import json
from unittest.mock import patch
from app import app
from services.monkeylearn_service import MonkeyLearnService


class TestMonkeyLearnService(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()

    @patch.object(MonkeyLearnService, 'text_sentiment')
    def test_monkeylearn_service(self, mock_text_sentiment):
        file_path = 'tests/fixtures/monkeylearn_positive.json'
        with open(file_path) as json_file:
            ml_data = json.load(json_file)
        
        mock_text_sentiment.return_value = ml_data

        service = MonkeyLearnService('Super positive great happy fun times')
        result = service.mood_value()

        self.assertEqual('Positive', result)


if __name__ == "__main__":
    unittest.main()
