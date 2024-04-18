from transformers import pipeline
from kserve import Model, ModelServer
from typing import Dict, Union
import logging

class SentimentAnalysis(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.load()

    def load(self):
        self.pipeline = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        # add log about payload
        logging.info("Start prediction")
        logging.info(payload)
        emotion = self.pipeline(payload['instances'][-1])

        logging.info("End prediction")
        return {"instances": emotion}

    def postprocess(self, result: Dict, headers: Dict[str, str] = None) -> Dict:
        # Find the label with the highest score
        highest_score_label = max(result["instances"][0], key=lambda x: x["score"])["label"]

        # Format the result as requested
        result = {"instances": [highest_score_label]}
        return result

if __name__ == "__main__":
    model = SentimentAnalysis("sentiment-analysis")
    ModelServer().start([model])