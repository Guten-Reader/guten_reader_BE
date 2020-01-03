import requests

class SpotifyService:

    #converts google_lang value to spotify valence value
    def spotify_sentiment_value(self, sentiment_value):
        converted_value = (sentiment_value + 1)/2
        return round(converted_value, 1)

    def recommend(self, access_token, user_id, sentiment_value):
        valence = self.spotify_sentiment_value(sentiment_value)
        spotify_recommendation = self.get_spotify_recommendation(access_token, valence)

        if spotify_recommendation.status_code == 200:
            body = spotify_recommendation.json()
            return {
                    'artist': body['tracks'][0]['artists'][0]["name"],
                    'track_id': body['tracks'][0]['id'],
                    'track_name': body['tracks'][0]['name']
                    }
        elif spotify_recommendation.status_code == 401:
            # 401 status code if access_token expired
            # add logic to make GET request to rails app for user's updated access_token
            # could use user_id or access_token to denote specific user
            # GET request returns updated access_token
            # use updated access_token to make new get_spotify_recommendation request
            # if second recommendation API sucessful then...
                # return track_id
            # if second_recommendation API fail then...
                # return error message

            #placeholder for invalid access_token sad path
            return "invalid token"
        else:
            return "invalid request"

    def get_spotify_recommendation(self, access_token, valence):
        params = {'valence': valence,
                  'seed_genres': 'classical',
                  'limit': 1}
        headers = {'Authorization': f'Bearer {access_token}'}
        request = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params)
        return request
