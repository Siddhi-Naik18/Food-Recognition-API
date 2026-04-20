from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import torch

MODEL_NAME = 'nateraw/food'
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Loading Model {MODEL_NAME} on {_device}...")

processor = ViTImageProcessor.from_pretrained(MODEL_NAME)
model =  ViTForImageClassification.from_pretrained(MODEL_NAME)
model.eval()

def classify_image(image: Image.Image) -> str:
    inputs = processor(images = image.convert("RGB"), return_tensors = "pt").to(_device)
    outputs = model(**inputs)
    pred_idx = outputs.logits.argmax(-1).item()
    label =  model.config.id2label[pred_idx]
    return label