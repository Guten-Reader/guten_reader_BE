from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from services.clean_text import clean_text

class GoogleLangService:
    def __init__(self, text):
        self.text = clean_text(text)

    def sentiment_analysis(self):
        client = language.LanguageServiceClient()
        document = types.Document(
            content=self.text,
            type=enums.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        return sentiment

    # def mood_tag(self, score):
    #     mood = 'Neutral'
    #     if score < -0.33:
    #         mood = 'Negative'
    #     elif score > 0.33:
    #         mood = 'Positive'
    #
    #     return mood

    def text_sentiment(self):
        sentiment = self.sentiment_analysis()
        score = sentiment.score
        # mood = self.mood_tag(score)
        # return {
        #     'text': self.text,
        #     'sentiment': {
        #         'mood': mood,
        #         'score': score,
        #         'magnitude': sentiment.magnitude
        #     }
        # }
        return score
