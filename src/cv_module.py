import requests
import base64
import json
import os

class CVModule:
    def __init__(self, api_key: str, model_id: str, version: str = "1"):
        self.api_key = api_key
        self.model_id = model_id
        self.version = version
        self.endpoint = f"https://app.roboflow.com/dog-feeder/detective-w9ja6/models/detective-w9ja6/1"

    def encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as f:
            img_bytes = f.read()
        return base64.b64encode(img_bytes).decode("utf-8")

    def predict(self, image_path: str, confidence: float = 0.5) -> dict:
        img_b64 = self.encode_image(image_path)
        data = {
            "api_key": self.api_key,
            "base64": img_b64,
            "confidence": confidence
        }
        resp = requests.post(self.endpoint, json=data)
        return resp.json()

if __name__ == "__main__":
    api = "YOUR_ROBOFLOW_API_KEY"
    model = "dog-feeder/detective-w9ja6"
    cv = CVModule(api_key=api, model_id=model, version="14")
    output = cv.predict("assets/test_image.jpg")
    print(json.dumps(output, indent=2))
