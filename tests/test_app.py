import unittest, json
from dotenv import load_dotenv, find_dotenv
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        load_dotenv(find_dotenv('.env', raise_error_if_not_found=True))
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()


    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'Guten-Reader API', response.data)
    

    def test_monkeylearn(self):
        data = {'text': 'This is super happy and positive'}
        response = self.app.get('/api/v1/monkeylearn',
                                data=json.dumps(data),
                                content_type='application/json')
        
        body = json.loads(response.data)[0]
        self.assertEqual(response.status_code, 200)
        self.assertIn('classifications', body)
        
        tag_name = body['classifications'][0]['tag_name']
        self.assertIn(tag_name, ['Positive', 'Neutral', 'Negative'])


if __name__ == "__main__":
    unittest.main()