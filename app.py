from flask import Flask, request, jsonify
from textblob import TextBlob

from services.googlelang_service import GoogleLangService
from services.monkeylearn_service import MonkeyLearnService

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
    sentiment = service.text_sentiment()
    return jsonify(sentiment)


if __name__ == '__main__':
    app.run(port=5000, debug=True)