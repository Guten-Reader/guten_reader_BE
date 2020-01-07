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

if __name__ == "__main__":
    unittest.main()