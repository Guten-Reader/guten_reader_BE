from flask import Flask, request, jsonify
from monkeylearn import MonkeyLearn
from textblob import TextBlob

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Guten-Reader API'


@app.route('/monkeylearn')
def monkeylearn():
    text = request.json['text']
    ml = MonkeyLearn('a99fe9ee2b2fcd0300543475b1f4205d6a20c400')
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
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print(sentiment)
    return jsonify({
        'score': sentiment.score,
        'magnitude': sentiment.magnitude
    })


if __name__ == '__main__':
    app.run(port=5000, debug=True)