import os
from flask import Flask, request, jsonify

from services.monkeylearn_service import MonkeyLearnService
from services.watson_service import WatsonService
from services.spotify_service import SpotifyService

app = Flask(__name__)

app.config.from_object(os.environ.get('APP_SETTINGS'))


@app.route('/')
def hello():
    return 'Guten-Reader API'

@app.route('/api/v1/watson')
def watson():
    text = request.json['text']
    service = WatsonService()
    sentiment = service.do_thing(text)
    return jsonify(sentiment)


@app.route('/api/v1/monkeylearn')
def monkeylearn():
    text = request.json['text']
    service = MonkeyLearnService(text)
    sentiment = service.text_sentiment()
    return jsonify(sentiment)


@app.route('/api/v1/recommendation', methods=["POST"])
def recommendation():
    body =  {} if request.get_data() == b'' else request.get_json()
    required_params = {'text', 'current_mood', 'access_token'}
    missing_params = list(required_params - set(body.keys()))

    if missing_params:
        return jsonify({'error': {'missing_params': missing_params}}), 400

    monkeylearn_service = MonkeyLearnService(body['text'])
    new_mood = monkeylearn_service.mood_value()

    if body['current_mood'] != new_mood:
        spotify_service = SpotifyService(body['access_token'], new_mood)
        result = spotify_service.recommend()
        return jsonify(result), result['status_code']
    else:
        return '', 204


if __name__ == '__main__':
    app.run()
