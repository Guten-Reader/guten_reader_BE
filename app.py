import os
from flask import Flask, request, jsonify
from monkeylearn import MonkeyLearn
from textblob import TextBlob

from services.googlelang_service import GoogleLangService

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Guten-Reader API'


@app.route('/monkeylearn')
def monkeylearn():
    text = request.json['text']
    ml = MonkeyLearn(os.environ['MONKEYLEARN_KEY'])
    response = ml.classifiers.classify(
        model_id='cl_pi3C7JiL',
        data=[text]
    )
    return jsonify(response.body)


@app.route('/textblob')
def textblob():
    body = request.json
    text = TextBlob(body['text'])
    return jsonify({'sentiment': text.sentiment})


@app.route('/googlelang')
def googlelang():
    text = request.json['text']
    service = GoogleLangService(text)
    return jsonify(service.text_sentiment())


if __name__ == '__main__':
    app.run(port=5000, debug=True)