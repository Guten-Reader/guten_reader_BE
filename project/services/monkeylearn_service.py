import os
from monkeylearn import MonkeyLearn
from project.services.clean_text import clean_text

class MonkeyLearnService:
    def __init__(self, text):
        self.text = clean_text(text)
        self.model = MonkeyLearn(os.environ['MONKEYLEARN_KEY'])
        self.model_id = os.environ['MONKEYLEARN_MODEL_ID']

    def text_sentiment(self):
        response = self.model.classifiers.classify(
            model_id=self.model_id,
            data=[self.text])
        return response.body

    def convert_mood_to_value(self, mood):
        if mood == 'Positive':
            return 1
        elif mood == 'Neutral':
            return 0.5
        return 0

    def mood_value(self):
        response = self.text_sentiment()
        mood = response[0]['classifications'][0]['tag_name']
        return self.convert_mood_to_value(mood)
