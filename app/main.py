from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
from io import BytesIO

from app.model import classify_image
from app.mealdb import get_ingredients_from_mealdb


MODEL_VERSION = '1.0'

app = FastAPI(
    title="Food Recognition API",
    version=MODEL_VERSION,
    description="Upload a food image -> get dish name + ingredients"
)

@app.get("/health")

def health_check():
    return {
        'status' : 'ok',
        'version' : MODEL_VERSION,
    }

@app.post("/predict")

async def predict(file: UploadFile = File(...)):
    if file.content_type not in ("image/png", "image/jpeg", "image/jpg"):
        raise HTTPException(status_code = 400, detail = "Only JPEG/PNG/JPG supported")
    
    image_bytes = await file.read()
    image = Image.open(BytesIO(image_bytes))

    label = classify_image(image)
    dish_name = label.replace("_", " ").title()

    ingredients, match_score = get_ingredients_from_mealdb(dish_name)

    if not ingredients or ingredients == ["No good match found for ingredients."]:
        raise HTTPException(status_code=404, detail=f"No ingredients found for {dish_name}")

    return {
        "dish": dish_name,
        "ingredients": ingredients,
        "match_score": match_score
    }

