import os
from flask import Flask, request, jsonify

from services.monkeylearn_service import MonkeyLearnService
from services.spotify_service import SpotifyService

app = Flask(__name__)

app.config.from_object(os.environ.get('APP_SETTINGS'))


@app.route('/')
def hello():
    return 'Guten-Reader API'


@app.route('/api/v1/monkeylearn')
def monkeylearn():
    text = request.json['text']
    service = MonkeyLearnService(text)
    sentiment = service.text_sentiment()
    return jsonify(sentiment)


@app.route('/api/v1/recommendation', methods=["POST"])
def recommendation():
    text = request.json['text']
    access_token = request.json['access_token']
    current_mood = request.json['current_mood']

    monkeylearn_service = MonkeyLearnService(text)
    sentiment = monkeylearn_service.mood_value()

    if current_mood != sentiment:
        spotify_service = SpotifyService()
        recommend_track = spotify_service.recommend(access_token, sentiment)

        return jsonify(recommend_track['result']), recommend_track['status_code']
    else:
        return jsonify({'message': 'No new tracks recommended'}), 200



if __name__ == '__main__':
    app.run()
