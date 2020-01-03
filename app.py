from flask import Flask, request, jsonify
from textblob import TextBlob

from services.googlelang_service import GoogleLangService
from services.monkeylearn_service import MonkeyLearnService
from services.spotify_service import SpotifyService

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Guten-Reader API'


@app.route('/monkeylearn')
def monkeylearn():
    text = request.json['text']
    service = MonkeyLearnService(text)
    sentiment = service.mood_tag()
    return jsonify(sentiment)


@app.route('/textblob')
def textblob():
    body = request.json
    text = TextBlob(body['text'])
    return jsonify({'sentiment': text.sentiment})


@app.route('/googlelang')
def googlelang():
    text = request.json['text']
    service = GoogleLangService(text)
    sentiment_value = service.text_sentiment()
    return jsonify(sentiment_value)

# returns recommedation for track, requires valid access token
@app.route('/recommendation')
def recommendation():
    text = request.json['text']
    access_token = request.json['access_token']
    user_id = request.json['user_id']

    google_service = GoogleLangService(text)
    sentiment_value = google_service.text_sentiment()

    spotify_service = SpotifyService()
    # takes in access_token for authorization, user_id for potential sad path
    recommend_track_id = spotify_service.recommend(access_token, user_id, sentiment_value)

    return jsonify(recommend_track_id)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
