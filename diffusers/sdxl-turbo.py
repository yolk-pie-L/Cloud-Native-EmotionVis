from diffusers import AutoPipelineForText2Image
from kserve import Model, ModelServer
from typing import Dict, Union
import base64
from io import BytesIO

class ImageModel(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.load()

    def load(self):
        self.pipeline = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo")
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        image = self.pipeline(prompt=payload['instances'][0], num_inference_steps=1, guidance_scale=0.0).images[0]
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return {"instances": img_str}


if __name__ == "__main__":
    model = ImageModel("sdxl-turbo")
    ModelServer().start([model])