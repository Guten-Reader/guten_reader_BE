import os
from services.clean_text import clean_text
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
# documentment: https://github.com/watson-developer-cloud/python-sdk

class WatsonService:
    def __init__(self, text):
        self.text = clean_text(text)
        self.authenticator = IAMAuthenticator(os.environ.get('WATSON_API'))

    def convert_to_mood(self, sentiment_value):
    #watson sentiment value on scale from -1.0 to 1.0
        if sentiment_value > 0.25:
            return "postive"
        elif sentiment_value < -0.25:
            return "negative"
        else:
            return "neutral"


    def get_sentiment(self):
        service = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator=self.authenticator )
        service.set_service_url(os.environ.get('WATSON_URL'))

        try:
            response = service.analyze(
                text=self.text,
                features=Features(sentiment=SentimentOptions())).get_result()
            sentiment_value = response['sentiment']['document']['score']
            return self.convert_to_mood(sentiment_value)
        except:
        # Error: not enough text for language id, Code: 422
        # if not enough text, return neutral
            return self.convert_to_mood(0.0)
