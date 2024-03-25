from kserve import Model, ModelServer
from typing import Dict, Union
import logging
from lingua import Language, LanguageDetectorBuilder

class Detector(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.load()

    def load(self):
        # Define languages for the detector
        languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH, Language.CHINESE,
                     Language.RUSSIAN]

        # Build the language detector
        self.detector = LanguageDetectorBuilder.from_languages(*languages).build()
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        # add log about payload
        logging.info("Start prediction")
        logging.info(payload)

        input_text = payload["instances"][0]
        output = self.detector.detect_language_of(input_text)
        language = output.iso_code_639_1.name
        # lower case
        language = language.lower()
        # Detect language of the given text
        logging.info("End prediction %s", language)
        return {"instances": [language, payload["instances"][0]]}


if __name__ == "__main__":
    model = Detector("lingua")
    ModelServer().start([model])
