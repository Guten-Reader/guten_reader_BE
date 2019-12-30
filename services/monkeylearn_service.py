import os
from monkeylearn import MonkeyLearn

class MonkeyLearnService:
    def __init__(self, text):
        self.text = text
        self.model = MonkeyLearn(os.environ['MONKEYLEARN_KEY'])
        self.model_id = os.environ['MONKEYLEARN_MODEL_ID']

    def text_sentiment(self):
        response = self.model.classifiers.classify(
            model_id=self.model_id,
            data=[self.text])
        return response.body