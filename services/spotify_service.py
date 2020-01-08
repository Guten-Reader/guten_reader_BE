import requests

class SpotifyService:

    def recommend(self, access_token, sentiment):
        spotify_recommendation = self.get_spotify_recommendation(access_token, sentiment)

        if spotify_recommendation.status_code == 200:
            body = spotify_recommendation.json()
        
            track_list = []
            for item in body['tracks']:
                track_list.append(item['uri'])
            print(track_list)

            return { 'result': { 'recommended_tracks': track_list, 'mood': sentiment}, 'status_code': 200 }
        elif spotify_recommendation.status_code == 401:
            return { 'result': { 'message': "The access token expired"}, 'status_code': 401}
        else:
            return { 'result': { 'message': "Bad request"}, 'status_code': 400 }

    def song_params(self, sentiment):
        params = {
            'seed_genres': 'classical',
            'limit': 10,
            }
        if sentiment == 'Positive':
            params['mode'] = 1
            params['valence'] = 1
        elif sentiment == 'Negative':
            params['mode'] = 0
            params['valence'] = 0
        else:
            params['valence'] = 0.5
        return params


    def get_spotify_recommendation(self, access_token, sentiment_value):
        params = self.song_params(sentiment_value)
        headers = {'Authorization': f'Bearer {access_token}'}
        request = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params)
        return request
