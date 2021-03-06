import unittest
import json
from unittest.mock import patch
from app import app
from services.monkeylearn_service import MonkeyLearnService
from services.watson_service import WatsonService
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from services.spotify_service import SpotifyService

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


    @patch.object(WatsonService, 'get_watson_text_analyze')
    def test_get_watson(self, mock_text_sentiment):
        file_path = 'tests/fixtures/watson_positive.json'
        with open(file_path) as json_file:
            ml_data = json.load(json_file)

        mock_text_sentiment.return_value = ml_data

        data = {
            'text': "after signalling to him to stop:\r\n\r\n'Tell me, Johann, what is tonight?'\r\n\r\nHe crossed himself, as he answered laconically: 'Walpurgis nacht.' Then he took out his watch, a great, old-fashioned German silver thing as big as a turnip, and looked at it, with his eyebrows gathered together and a little impatient shrug of his shoulders. I realised that this was his way of respectfully protesting against the unnecessary delay, and sank back in the carriage, merely motioning him to proceed. He started off rapidly, as if to make up for lost time. Every now and then the horses seemed to throw up their"
        }

        response = self.app.get('/api/v1/watson',
                                data=json.dumps(data),
                                content_type='application/json')

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json)


    @patch('services.spotify_service.requests.get')
    @patch.object(WatsonService, 'get_watson_text_analyze')
    def test_POST_recommendation(self, mock_text_sentiment, mock_get):
        file_path = 'tests/fixtures/watson_positive.json'
        with open(file_path) as json_file:
            ml_data = json.load(json_file)

        mock_text_sentiment.return_value = ml_data

        file_path = 'tests/fixtures/spotify_tracks.json'
        with open(file_path) as json_file:
            tracks_data = json.load(json_file)

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = tracks_data

        data = {
            'text': 'Super positive great happy fun awesome great wonderful times',
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

        new_data = {
            'text': 'Super positive great happy fun times',
            'current_mood': 1,
            'access_token': 'totally-real-access-token',
            'genre': 'classical'
        }

        response = self.app.post('/api/v1/recommendation',
                                data=json.dumps(new_data),
                                content_type='application/json')

        self.assertEqual(204, response.status_code)


    @patch('services.spotify_service.requests.get')
    @patch.object(WatsonService, 'get_watson_text_analyze')
    def test_POST_recommendation_called_with_specific_params(self, mock_sentiment, mock_get):
        # Set up mock functions
        file_path = 'tests/fixtures/watson_positive.json'
        with open(file_path) as json_file:
            ml_data = json.load(json_file)

        mock_sentiment.return_value = ml_data

        file_path = 'tests/fixtures/spotify_tracks.json'
        with open(file_path) as json_file:
            tracks_data = json.load(json_file)

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = tracks_data

        # Check that Spotify API is called with correct parameters when genre setting is 'classical'
        data = {
            'text': 'Super positive great happy fun awesome great wonderful times',
            'current_mood': 0,
            'access_token': 'totally-real-access-token',
            'genre': 'classical'
        }

        response = self.app.post('/api/v1/recommendation',
                                 data=json.dumps(data),
                                 content_type='application/json')

        mock_get.assert_called_with(
            'https://api.spotify.com/v1/recommendations',
            headers={'Authorization': 'Bearer totally-real-access-token'},
            params={
                'valence': 1,
                'mode': 1,
                'seed_genres': 'classical',
                'limit': 10
            }
        )

        # Check that Spotify API is called with correct parameters when genre setting is 'piano'
        data2 = {
            'text': 'Super positive great happy fun awesome great wonderful times',
            'current_mood': 0,
            'access_token': 'totally-real-access-token',
            'genre': 'piano'
        }

        response = self.app.post('/api/v1/recommendation',
                                 data=json.dumps(data2),
                                 content_type='application/json')

        mock_get.assert_called_with(
            'https://api.spotify.com/v1/recommendations',
            headers={'Authorization': 'Bearer totally-real-access-token'},
            params={
                'valence': 1,
                'mode': 1,
                'seed_genres': 'piano',
                'limit': 10
            }
        )

        # Check that Spotify API is called with correct parameters when genre setting is 'electronic'
        data3 = {
            'text': 'Super positive great happy fun awesome great wonderful times',
            'current_mood': 0,
            'access_token': 'totally-real-access-token',
            'genre': 'electronic'
        }

        response = self.app.post('/api/v1/recommendation',
                                 data=json.dumps(data3),
                                 content_type='application/json')

        mock_get.assert_called_with(
            'https://api.spotify.com/v1/recommendations',
            headers={'Authorization': 'Bearer totally-real-access-token'},
            params={
                'valence': 1,
                'mode': 1,
                'seed_genres': 'idm',
                'limit': 10
            }
        )


if __name__ == "__main__":
    unittest.main()
