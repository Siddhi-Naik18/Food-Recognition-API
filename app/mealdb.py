import requests
from rapidfuzz import fuzz

def get_ingredients_from_mealdb(meal_name: str) -> list[str]:
    search_query = meal_name.replace("_", " ").lower()
    all_meals= {}
    categories_url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    try:
        categories = requests.get(categories_url).json().get("meals", [])
        for category in categories:
            category_name = category['strCategory']
            meals_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category_name}"
            meals_in_cat = requests.get(meals_url).json().get("meals", [])
            for meal in meals_in_cat:
                all_meals[meal['strMeal']] = meal['idMeal']
    except requests.exceptions.RequestException as e:
        return [f"Error connecting to TheMealDB API: {e}"]

    if not all_meals:
        return ["No meals found to perform a search."]

    best_match_score = 0
    best_match_meal_id = None
    
    for meal_name_db, meal_id in all_meals.items():
        current_score = fuzz.partial_ratio(search_query, meal_name_db.lower())
        
        if current_score > best_match_score:
            best_match_score = current_score
            best_match_meal_id = meal_id

    if best_match_meal_id and best_match_score > 75:  # 75 is a reasonable threshold
        # print(f"Best match found with a score of {best_match_score}. Fetching ingredients...")
        detail_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={best_match_meal_id}"
        detail_resp = requests.get(detail_url)
        meal_detail = detail_resp.json().get("meals", [None])[0]

        if meal_detail:
            ingredients = []
            for i in range(1, 21):
                ingredient = meal_detail.get(f"strIngredient{i}")
                measure = meal_detail.get(f"strMeasure{i}")
                if ingredient and ingredient.strip():
                    ingredients.append(f"- {ingredient} ({measure.strip()})")
            return ingredients, best_match_score
    
    return ["No good match found for ingredients."]
