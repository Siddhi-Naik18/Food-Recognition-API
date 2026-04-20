from PIL import Image
from app.model import classify_image

img = Image.open("images/burger.jpg")
label = classify_image(img)
print("Predicted label: ", label)