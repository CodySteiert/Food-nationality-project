# Food api
import requests

class MealDB:
    def __init__(self, endOfEndpoint):
        self.endpoint = f'https://www.themealdb.com/api/json/v1/1/{endOfEndpoint}'
        self.meals = []
        self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.endpoint)
        if response.status_code == 200:
            data = response.json()
            self.parse_data(data)
        else:
            print(f"Error: {response.status_code}")

    def parse_data(self, data):
        meals = data.get('meals', [])
        for meal in meals:
            meal_info = {
                'id': meal.get('idMeal'),
                'name': meal.get('strMeal'),
                'category': meal.get('strCategory'),
                'area': meal.get('strArea'),
                'instructions': meal.get('strInstructions'),
                'thumbnail': meal.get('strMealThumb'),
                'tags': meal.get('strTags'),
                'youtube': meal.get('strYoutube'),
                'ingredients': self.get_ingredients(meal)
            }
            self.meals.append(meal_info)

    def get_ingredients(self, meal):
        ingredients = []
        for i in range(1, 21):
            ingredient = meal.get(f'strIngredient{i}')
            if ingredient:
                ingredients.append(ingredient)
        return ingredients

    def get_meals(self):
        return self.meals

# Example Usage
meal_db = MealDB('search.php?f=a')
meals = meal_db.get_meals()
for meal in meals:
    print(meal)
