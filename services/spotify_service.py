import requests

class SpotifyService:

    def recommend(self, access_token, user_id, sentiment_value):
        spotify_recommendation = self.get_spotify_recommendation(access_token, sentiment_value)

        if spotify_recommendation.status_code == 200:
            body = spotify_recommendation.json()
            return { 'message': {
                    'artist': body['tracks'][0]['artists'][0]["name"],
                    'track_id': body['tracks'][0]['id'],
                    'track_name': body['tracks'][0]['name'],
                    'track_uri': body['tracks'][0]['uri']
                    }, 'status_code': 200 }
        elif spotify_recommendation.status_code == 401:
            request = requests.get(f'https://guten-server.herokuapp.com/api/v1/access_token/{user_id}')

            if request.status_code == 200:
                access_token = request.json()['access_token']
                return self.recommend(access_token, user_id, sentiment_value)
            else:
                return { 'message': f"User:{user_id} does not exist", 'status_code': 404}
        else:
            return { 'message': "Bad request", 'status_code': 400 }

    def song_params(self, sentiment_value):
        params = {
            'valence': sentiment_value,
            'seed_genres': 'classical',
            'limit': 1,
        }
        if sentiment_value == 1:
            params['mode'] = 1
        elif sentiment_value == 0:
            params['mode'] = 0

        return params


    def get_spotify_recommendation(self, access_token, sentiment_value):
        params = self.song_params(sentiment_value)
        headers = {'Authorization': f'Bearer {access_token}'}
        request = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params)
        return request
