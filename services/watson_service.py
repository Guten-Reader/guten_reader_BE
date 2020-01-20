import os
from services.clean_text import clean_text
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

class WatsonService:
    def __init__(self, text):
        self.text = clean_text(text)

    def convert_to_spotify_valence(self, sentiment_value):
        if sentiment_value > 0.25:
            return 1
        elif sentiment_value < -0.25:
            return 0
        else:
            return 0.5

    def get_sentiment_value(self):
        response = self.get_watson_text_analyze()
        if response.status_code == 200:
            sentiment_value = response.get_result()['sentiment']['document']['score']
            return self.convert_to_spotify_valence(sentiment_value)
        else:
            return self.convert_to_spotify_valence(0.0)


    def get_watson_text_analyze(self):
        service = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator= IAMAuthenticator(os.environ.get('WATSON_API')) )
        service.set_service_url(os.environ.get('WATSON_URL'))
        try:
            response = service.analyze(
                text=self.text,
                features=Features(sentiment=SentimentOptions()))
            return response
        except:
            return response
