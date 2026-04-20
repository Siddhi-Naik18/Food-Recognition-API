from app.mealdb import get_ingredients_from_mealdb

dish = "Club sandwich"
ingredients = get_ingredients_from_mealdb(dish)

print(f"Dish: {dish}")
print("Ingredients:")
for ing in ingredients:
    print("-", ing)