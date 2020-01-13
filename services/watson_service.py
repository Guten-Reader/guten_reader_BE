import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

class WatsonService:

    def do_thing(self, text):
        authenticator = IAMAuthenticator(os.environ.get('WATSON_API'))
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator=authenticator
        )

        natural_language_understanding.set_service_url(os.environ.get('WATSON_URL'))

        response = natural_language_understanding.analyze(
            text=text,
            features=Features(
                sentiment=SentimentOptions()
            )
        )
        # API call working, need error handling for 422 (Error: not enough text for language id)
        return response.get_result()
