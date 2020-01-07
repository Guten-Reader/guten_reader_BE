import unittest

from app import app
from services.spotify_service import SpotifyService


class TestSpotifyService(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestingConfig')
        self.app = app.test_client()

    def test_song_params_for_positive_mood(self):
        service = SpotifyService()
        result = service.song_params('Positive')
        expected = {
            'valence': 1,
            'mode': 1,
            'seed_genres': 'classical',
            'limit': 1
        }
        self.assertDictEqual(expected, result)

    def test_song_params_for_neutral_mood(self):
        service = SpotifyService()
        result = service.song_params('Neutral')
        expected = {
            'valence': 0.5,
            'seed_genres': 'classical',
            'limit': 1
        }
        self.assertDictEqual(expected, result)

    def test_song_params_for_negative_mood(self):
        service = SpotifyService()
        result = service.song_params('Negative')
        expected = {
            'valence': 0,
            'mode': 0,
            'seed_genres': 'classical',
            'limit': 1
        }
        self.assertDictEqual(expected, result)

if __name__ == "__main__":
    unittest.main()