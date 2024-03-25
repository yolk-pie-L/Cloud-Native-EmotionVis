from transformers import pipeline
from kserve import Model, ModelServer
from typing import Dict, Union
import logging


class Detector(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.load()

    def load(self):
        self.pipeline = pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection-roberta-base-language-detection")
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        # add log about payload
        logging.info("Start prediction")
        logging.info(payload)

        input_text = payload["instances"]
        output = self.pipeline(input_text, top_k=1, truncation=True)

        language = output[0][0]["label"]
        logging.info("End prediction %s", language)
        return {"instances": [language]}


if __name__ == "__main__":
    model = Detector("xlm-roberta-base-language-detection-roberta-base-language-detection")
    ModelServer().start([model])
