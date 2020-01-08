import os
from monkeylearn import MonkeyLearn
from services.clean_text import clean_text

class MonkeyLearnService:
    def __init__(self, text):
        self.text = clean_text(text)
        self.model = MonkeyLearn(os.environ.get('MONKEYLEARN_KEY'))
        self.model_id = os.environ.get('MONKEYLEARN_MODEL_ID')

    def text_sentiment(self):
        response = self.model.classifiers.classify(
            model_id=self.model_id,
            data=[self.text])
        return response.body

    def mood_value(self):
        response = self.text_sentiment()
        mood = response[0]['classifications'][0]['tag_name']
        return mood
