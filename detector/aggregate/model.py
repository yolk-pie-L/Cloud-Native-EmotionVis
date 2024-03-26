from kserve import Model, ModelServer
from typing import Dict, Union
import logging


class Detector(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        # log paylod
        logging.info(f"Payload: {payload}")
        # Analyze the instances to determine the most frequent instance
        instances_counter = {}

        for key in payload:
            instances = tuple(payload[key]["instances"])  # Convert the list to a tuple so it can be used as a dictionary key
            if instances in instances_counter:
                instances_counter[instances] += 1
            else:
                instances_counter[instances] = 1

        # Find the instance with the highest count
        most_frequent_instance = max(instances_counter, key=instances_counter.get)

        result = {"instances": list(most_frequent_instance)}
        logging.info(f"Result: {result}")
        return result


if __name__ == "__main__":
    model = Detector("aggregate")
    ModelServer().start([model])
