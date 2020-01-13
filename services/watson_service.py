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


    def get_sentiment(self):
        service = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator=self.authenticator )
        service.set_service_url(os.environ.get('WATSON_URL'))

        try:
            response = service.analyze(
                text=self.text,
                features=Features(sentiment=SentimentOptions())).get_result()
            return response['sentiment']['document']['score']
        except:
        # "Error: not enough text for language id, Code: 422"
            return 0.0
