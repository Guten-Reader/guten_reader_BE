import unittest
import json
from unittest.mock import patch
from app import app
from services.spotify_service import SpotifyService


class TestSpotifyService(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()


    def test_song_params_for_positive_mood(self):
        service = SpotifyService('token', 1)
        result = service.song_params()
        expected = {
            'valence': 1,
            'mode': 1,
            'seed_genres': 'classical',
            'limit': 10
        }
        self.assertDictEqual(expected, result)


    def test_song_params_for_neutral_mood(self):
        service = SpotifyService('token', 0.5)
        result = service.song_params()
        expected = {
            'valence': 0.5,
            'seed_genres': 'classical',
            'limit': 10
        }
        self.assertDictEqual(expected, result)


    def test_song_params_for_negative_mood(self):
        service = SpotifyService('token', 0)
        result = service.song_params()
        expected = {
            'valence': 0,
            'mode': 0,
            'seed_genres': 'classical',
            'limit': 10
        }
        self.assertDictEqual(expected, result)

    
    def test_song_params_for_piano_genre(self):
        service = SpotifyService('token', 0.5, 'piano')
        result = service.song_params()
        expected = {
            'valence': 0.5,
            'seed_genres': 'piano',
            'limit': 10
        }
        self.assertDictEqual(expected, result)

    
    def test_song_params_for_electronic_genre(self):
        service = SpotifyService('token', 0.5, 'electronic')
        result = service.song_params()
        expected = {
            'valence': 0.5,
            'seed_genres': 'idm',
            'limit': 10
        }
        self.assertDictEqual(expected, result)


    @patch('services.spotify_service.requests.get')
    def test_recommend_happy_path(self, mock_get):
        file_path = 'tests/fixtures/spotify_tracks.json'
        with open(file_path) as json_file:
            tracks_data = json.load(json_file)

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = tracks_data

        service = SpotifyService('token', 'Positive')
        result = service.recommend()

        expected = {
            'mood': 'Positive',
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

        self.assertEqual(200, result['status_code'])
        self.assertDictEqual(expected, result)


    @patch('services.spotify_service.requests.get')
    def test_recommend_sad_path(self, mock_get):
        file_path = 'tests/fixtures/spotify_expired_token.json'
        with open(file_path) as json_file:
            message = json.load(json_file)

        mock_get.return_value.status_code = 401
        mock_get.return_value.json.return_value = message

        service = SpotifyService('token', 'Positive')
        result = service.recommend()

        expected = { 'message': 'The access token expired', 'status_code': 401 }

        self.assertEqual(401, result['status_code'])
        self.assertDictEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
