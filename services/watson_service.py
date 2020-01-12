import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class WatsonService:

    def do_thing(self, text):
        authenticator = IAMAuthenticator(os.environ.get('WATSON_API'))
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator=authenticator
        )

        natural_language_understanding.set_service_url(os.environ.get('WATSON_URL'))

        response = natural_language_understanding.analyze( url='www.ibm.com', features=Features(categories=CategoriesOptions(limit=3))).get_result()

        print(json.dumps(response, indent=2))
