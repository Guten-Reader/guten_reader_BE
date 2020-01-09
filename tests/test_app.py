import unittest
import json
from unittest.mock import patch
from app import app
from services.monkeylearn_service import MonkeyLearnService

class TestHello(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()


    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'Guten-Reader API', response.data)


    @patch.object(MonkeyLearnService, 'text_sentiment')
    def test_get_monkeylearn(self, mock_text_sentiment):
        file_path = 'tests/fixtures/monkeylearn_positive.json'
        with open(file_path) as json_file:
            ml_data = json.load(json_file)
        
        mock_text_sentiment.return_value = ml_data

        data = {'text': 'Super positive great happy fun times'}
        response = self.app.get('/api/v1/monkeylearn',
                                data=json.dumps(data),
                                content_type='application/json')

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(ml_data[0], response.json[0])


if __name__ == "__main__":
    unittest.main()
