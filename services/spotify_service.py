class SpotifyService:
    def spotify_sentiment_value(google_lang_sentiment_value):
        converted_value = (sentiment_value + 1)/2
        return converted_value

    def recommendation(access_token, user_id, sentiment_value):
        valence = spotify_sentiment_value(senitment_value)
         # GET https://api.spotify.com/v1/recommendations?seed_genres=classical&limit=1&valence=[SPOTIFY_SENTIMENT_VALUE]
         # Needs Authorization in header
         # if Authorization success
            # parse JSON for track ID
            # return track ID

         # if Authorization fails
            # make GET request to rails app to get new access token
            # retry Spotify recommendation API call
            # parse JSOn for track ID
            # return track ID
        return track_id
