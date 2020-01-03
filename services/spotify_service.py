import requests
import os

class SpotifyService:

    #converts google_lang value to spotify valence value
    def spotify_sentiment_value(self, sentiment_value):
        converted_value = (sentiment_value + 1)/2
        return round(converted_value, 1)

    def recommend_track(self, access_token, user_id, sentiment_value):
        valence = self.spotify_sentiment_value(sentiment_value)
        params = {'valence': valence,
                  'seed_genres': 'classical',
                  'limit': 1}
        headers = {'Authorization': f'Bearer {access_token}'}
        request = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params)
        body = request.json()
        return body['tracks'][0]['id']

        # if access token invalid then...
            # make GET request to rails app to get new access token
            # could user user_id or maybe access_token to determine which access_token to update
            # once access_token updated, retries Spotify recommendation API call above
            # if second Spotify recommedation API sucessful then...
                # parse JSON for track ID
                # return track ID
            # if second Spotify recommendation API fail then ...
                # send message call could not be completed
