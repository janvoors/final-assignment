import pandas as pd
from rapidfuzz import fuzz

recipes = pd.read_csv("recipes.csv")
recipes.head()

print("\nRecipe Assistant\n")

user_input = input("What ingredients do you have? ").strip()
user_ingredients = [i.strip().lower() for i in user_input.split(",")]

meal_type = input("Meal type? (breakfast/lunch/dinner or enter to skip): ").strip().lower()
if meal_type == "":
    meal_type = None

# filter properly
filtered_recipes = recipes.copy()

if meal_type:
    filtered_recipes = filtered_recipes[
        filtered_recipes["meal_type"].str.lower() == meal_type
    ]

scored = []

# iterate correctly
for _, r in filtered_recipes.iterrows():
    
    # split ingredients string into list
    recipe_ings = [i.strip().lower() for i in r["ingredients"].split(",")]

    matches = []

    for ui in user_ingredients:
        for ri in recipe_ings:
            if fuzz.partial_ratio(ui, ri) >= 80:
                matches.append(ri)
                break

    score = len(matches) / len(recipe_ings) if recipe_ings else 0

    if score > 0:
        scored.append((score, matches, r))

if not scored:
    print("\nNo matching recipes found.\n")
else:
    scored.sort(reverse=True, key=lambda x: x[0])
    best_score, matched_ings, recipe = scored[0]

    print(f"\nBest match: {recipe['title']} ({recipe['meal_type']})")
    print(f"Match score: {round(best_score, 2)}")
    print(f"You have: {matched_ings}")

    recipe_ingredients = [i.strip() for i in recipe["ingredients"].split(",")]

    prompt = f"""
You are a helpful cooking assistant.

User has these ingredients:
{", ".join(user_ingredients)}

Recipe: {recipe['title']} ({recipe['meal_type']})

Ingredients in recipe:
{", ".join(recipe_ingredients)}

User already has:
{", ".join(matched_ings)}

Tasks:
1. List missing ingredients
2. Suggest substitutions if possible
3. Provide simple step-by-step instructions
4. Keep it concise
"""

    use_llm = input("\nGenerate full recipe with LLM? (y/n): ").lower()

    if use_llm == "y":
        import ollama

        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        print(response["message"]["content"])

print("\n" + "="*50 + "\n")