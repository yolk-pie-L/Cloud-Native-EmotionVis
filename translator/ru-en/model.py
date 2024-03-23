from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from kserve import Model, ModelServer
from typing import Dict, Union
import logging


class Translator(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.load()

    def load(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
        self.tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        # add log about payload
        logging.info("Start prediction")
        logging.info(payload)

        input_text = payload["instances"][0]
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        decoded = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        logging.info("End prediction %s", decoded)
        return {"instances": [decoded]}


if __name__ == "__main__":
    model = Translator("ru-en")
    ModelServer().start([model])
