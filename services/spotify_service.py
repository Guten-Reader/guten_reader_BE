import requests

class SpotifyService:
    def __init__(self, access_token, sentiment):
        self.access_token = access_token
        self.sentiment = sentiment


    def recommend(self):
        spotify_recommendation = self.get_spotify_recommendation()
        if spotify_recommendation.status_code == 200:
            body = spotify_recommendation.json()
            return self._recommended_tracks(body)
        elif spotify_recommendation.status_code == 401:
            return self._expired_token()


    def song_params(self):
        params = {
            'seed_genres': 'classical',
            'limit': 10 }
        if self.sentiment == 'Positive':
            params['mode']    = 1
            params['valence'] = 1
        elif self.sentiment == 'Negative':
            params['mode']    = 0
            params['valence'] = 0
        else:
            params['valence'] = 0.5
        return params


    def get_spotify_recommendation(self):
        params = self.song_params()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(
            'https://api.spotify.com/v1/recommendations',
            headers=headers,
            params=params)
        return response
    

    def _expired_token(self):
        return { 'message': 'The access token expired', 'status_code': 401 }
    

    def _recommended_tracks(self, body):
        track_list = []
        for item in body['tracks']:
            track_list.append(item['uri'])
        return {
            'recommended_tracks': track_list,
            'mood': self.sentiment,
            'status_code': 200
        }