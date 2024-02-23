import csv
from collections import defaultdict

# Initialize a defaultdict to count occurrences of each ingredient
ingredient_counts = defaultdict(int)

# Open the dataset file and parse it
with open('/Users/bestc/Code Projects/COMO AI/data/raw/RecipeNLG_dataset.csv', 'r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    # Extract ingredients list, assuming they're stored in the 'ingredients' column
    ingredients = eval(row['ingredients'])  # Use eval to convert string list representation to list
    for ingredient in ingredients:
      # Increment the count for each ingredient found
      ingredient_counts[ingredient.lower()] += 1

# Now, save the ingredient counts to a new file
with open('ingredient_counts.txt', 'w') as out_file:
  for ingredient, count in ingredient_counts.items():
    out_file.write(f"{ingredient}: {count}\n")

print("Ingredient counts saved to ingredient_counts.txt.")
