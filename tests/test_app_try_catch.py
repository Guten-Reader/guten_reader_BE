import unittest
import json
from unittest.mock import patch
from app import app
from services.monkeylearn_service import MonkeyLearnService
from services.watson_service import WatsonService
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from services.spotify_service import SpotifyService

class TestWatsonOutage(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()


    @patch('services.spotify_service.requests.get')
    @patch.object(WatsonService, 'get_watson_text_analyze')
    @patch.object(MonkeyLearnService, 'text_sentiment')
    def test_POST_recommendation_watson_outage(self, mock_monkeylearn, mock_watson, mock_spotify):

        file_path = 'tests/fixtures/monkeylearn_positive.json'
        with open(file_path) as json_file:
            monkeylearn_data = json.load(json_file)

        mock_monkeylearn.return_value.status_code = 200
        mock_monkeylearn.return_value = monkeylearn_data

        mock_watson.return_value.status_code = 504

        file_path = 'tests/fixtures/spotify_tracks.json'
        with open(file_path) as json_file:
            tracks_data = json.load(json_file)

        mock_spotify.return_value.status_code = 200
        mock_spotify.return_value.json.return_value = tracks_data


        data = {
            'text': 'Super positive great happy fun awesome great wonderful times wonderful',
            'current_mood': 0,
            'access_token': 'totally-real-access-token',
            'genre': 'classical'
        }

        response = self.app.post('/api/v1/recommendation',
                                data=json.dumps(data),
                                content_type='application/json')

        expected = {
            'mood': 1,
            'recommended_tracks': [
                'spotify:track:6PrKZUXJPmBiobMN44yR8Y',
                'spotify:track:1IM8x4lxZVOOP9gpQD6c5s',
                'spotify:track:6W4OTAu8XW5p2Ac4aAIUDl',
                'spotify:track:4W18MvpMRFd58dSVidxdO9',
                'spotify:track:2TkGYqnVFS0T5u2PYN6JQS',
                'spotify:track:55xly70WJY1cx5qsoogaqs',
                'spotify:track:1lIcdDpGlc2mO2LYA0f5KM',
                'spotify:track:2GAcOueBAbwU0kgaXKVAdM',
                'spotify:track:4IDn6FlDFosueSOH0mfExb',
                'spotify:track:0NwyxchEawg8eL8EO2A1DZ'],
            'status_code': 200}

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(expected, response.json)


if __name__ == "__main__":
    unittest.main()
