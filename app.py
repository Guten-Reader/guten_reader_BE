from flask import Flask, request, jsonify

from services.monkeylearn_service import MonkeyLearnService
from services.spotify_service import SpotifyService

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return 'Guten-Reader API'


@app.route('/api/v1/monkeylearn')
def monkeylearn():
    text = request.json['text']
    service = MonkeyLearnService(text)
    sentiment = service.text_sentiment()
    return jsonify(sentiment)


@app.route('/api/v1/recommendation')
def recommendation():
    text = request.json['text']
    access_token = request.json['access_token']
    user_id = request.json['user_id']

    monkeylearn_service = MonkeyLearnService(text)
    sentiment_value = monkeylearn_service.mood_value()

    spotify_service = SpotifyService()
    # takes in access_token for authorization, user_id for potential sad path
    recommend_track = spotify_service.recommend(access_token, user_id, sentiment_value)

    return jsonify(recommend_track)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
