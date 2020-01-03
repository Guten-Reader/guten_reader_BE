import requests
import os

class SpotifyService:

    #converts google_lang value to spotify valence value
    def spotify_sentiment_value(self, sentiment_value):
        converted_value = (sentiment_value + 1)/2
        return round(converted_value, 1)

    def recommend(self, access_token, user_id, sentiment_value):
        valence = self.spotify_sentiment_value(sentiment_value)
        params = {'valence': valence,
                  'seed_genres': 'classical',
                  'limit': 1}
        headers = {'Authorization': f'Bearer {access_token}'}
        request = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params)
        body = request.json()
        return body['tracks'][0]['id']

        # if access token invalid
            # make GET request to rails app to get new access token
            # retry Spotify recommendation API call
            # parse JSON for track ID
            # return track ID
