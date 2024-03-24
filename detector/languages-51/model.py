from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
from kserve import Model, ModelServer
from typing import Dict, Union
import logging

class Detector(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.load()

    def load(self):
        self.model_name = 'qanastek/51-languages-classifier'
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, cache_dir="/tmp")
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, cache_dir="/tmp")
        self.classifier = TextClassificationPipeline(model=self.model, tokenizer=self.tokenizer)
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        # add log about payload
        logging.info("Start prediction")
        logging.info(payload)

        input_text = payload["instances"][0]
        output = self.classifier(input_text)

        language = output[0]["label"]
        logging.info("End prediction %s", language)
        return {"instances": [language]}


if __name__ == "__main__":
    model = Detector("languages-51")
    ModelServer().start([model])
