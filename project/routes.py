from project import app
from flask import request, jsonify
from project.services.monkeylearn_service import MonkeyLearnService
from project.services.spotify_service import SpotifyService


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