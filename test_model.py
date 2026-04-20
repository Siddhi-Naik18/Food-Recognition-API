from transformers import ViTImageProcessor, ViTForImageClassification

print("Loading processor...")
processor = ViTImageProcessor.from_pretrained("nateraw/food")

print("Loading model...")
model = ViTForImageClassification.from_pretrained("nateraw/food")

print("Model loaded successfully! Number of labels:", len(model.config.id2label))
