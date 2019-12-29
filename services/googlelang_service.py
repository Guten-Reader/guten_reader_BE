from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

class GoogleLangService:
    def __init__(self, text):
        self.text = text

    def sentiment_analysis(self):
        client = language.LanguageServiceClient()
        document = types.Document(
            content=self.text,
            type=enums.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        return sentiment

    def text_sentiment(self):
        sentiment = self.sentiment_analysis()
        return {
            'score': sentiment.score,
            'magnitude': sentiment.magnitude
        }
        