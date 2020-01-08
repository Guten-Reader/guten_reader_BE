import unittest, json

from app import app

class TestRecommendationSadPath(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()

    def test_recommendation_missing_single_param(self):
        data = {
            "current_mood": "Negative",
            "access_token": "this-is-totally-an-access-token"
        }
        response = self.app.post('/api/v1/recommendation',
                                data=json.dumps(data),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)
        
        data = response.get_json()
        error_response = {"error": {"missing_params": ["text"]}}
        self.assertDictEqual(error_response, data)

    def test_recommendation_missing_multiple_params(self):
        data = {}
        response = self.app.post('/api/v1/recommendation',
                                data=json.dumps(data),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)
        
        data = response.get_json()
        data_missing_params = set(data['error']['missing_params'])
        expected_missing_params = set(["text", "current_mood", "access_token"])
        self.assertSetEqual(expected_missing_params, data_missing_params)

    def test_recommendation_with_empty_body(self):
        response = self.app.post('/api/v1/recommendation',
                                data='',
                                content_type='application/json')
        self.assertEqual(400, response.status_code)
        
        data = response.get_json()
        data_missing_params = set(data['error']['missing_params'])
        expected_missing_params = set(["text", "current_mood", "access_token"])
        self.assertSetEqual(expected_missing_params, data_missing_params)


if __name__ == "__main__":
    unittest.main()