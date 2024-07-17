class Recipe:
    def __init__(self, name, ingredients, steps, level):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.level = level

    def show_info(self):
        print(f"Recipe: {self.name}\nIngredients:")
        for ingredient in self.ingredients:
            print(f"• {ingredient}")
        print("\nSteps:")
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step}")
        print(f"Difficulty level: {self.level}")


# Recipe list:
recipes = [
    Recipe(
        "Scrambled Eggs",
        [
            "2 eggs",
            "2 tablespoons milk",
            "Salt and pepper to taste",
            "1 tablespoon butter"
        ],
        [
            "Beat the eggs with milk, salt, and pepper in a bowl.",
            "Heat butter in a pan over medium heat.",
            "Pour the egg mixture into the pan.",
            "Stir gently with a spatula until eggs are set and slightly runny.",
            "Serve immediately."
        ],
        "\nEasy 😎"
    ),
    Recipe(
        "Pancakes",
        [
            "1 cup flour",
            "2 tablespoons sugar",
            "1 teaspoon baking powder",
            "1/2 teaspoon baking soda",
            "1/2 teaspoon salt",
            "1 cup buttermilk",
            "1 egg",
            "2 tablespoons melted butter"
        ],
        [
            "In a bowl, mix flour, sugar, baking powder, baking soda, and salt.",
            "In another bowl, whisk together buttermilk, egg, and melted butter.",
            "Pour the wet ingredients into the dry ingredients and stir until combined.",
            "Heat a pan over medium heat and grease it lightly.",
            "Pour batter onto the pan and cook until bubbles form on the surface, then flip and cook until golden brown.",
            "Serve with syrup or toppings of choice."
        ],
        "\nMedium 😤"
    ),
    Recipe(
        "Grilled Cheese Sandwich",
        [
            "2 slices of bread",
            "2 slices of cheese",
            "1 tablespoon butter",
        ],
        [
            "Butter one side of each bread slice.",
            "Place one slice, buttered side down, in a hot skillet.",
            "Add cheese slices on top.",
            "Place the other slice of bread, buttered side up, on the cheese.",
            "Cook until bread is golden brown and cheese is melted, flipping once."
        ],
        "\nEasy 😎"
    ),
    Recipe(
        "Fruit Smoothie",
        [
            "1 banana",
            "1 cup mixed berries (fresh or frozen)",
            "1 cup milk or juice",
            "1 tablespoon honey (optional)"
        ],
        [
            "Combine all ingredients in a blender.",
            "Blend until smooth.",
            'Pour into a glass and serve immediately.'
        ],
        "\nEasy 😎"
    ),
    Recipe(
        "Pasta with Garlic and Olive Oil",
        [
            "200g spaghetti",
            "3 cloves garlic, thinly sliced",
            '1/4 cup olive oil',
            "Salt and pepper to taste",
            "Grated Parmesan cheese (optional)"
        ],
        [
            "Cook spaghetti according to package instructions.",
            "In a pan, heat olive oil over medium heat.",
            "Add garlic and cook until golden.",
            "Drain the pasta and add it to the pan with garlic and oil.",
            "Toss well and season with salt and pepper.",
            "Serve with grated Parmesan if desired."
        ],
        "\nMedium 😤"
    ),
    Recipe(
        "Chicken Stir-Fry",
        [
            "2 chicken breasts, sliced thinly",
            "2 tablespoons soy sauce",
            "1 tablespoon sesame oil",
            "1 bell pepper, sliced",
            "1 carrot, sliced",
            "1 onion, sliced",
            "2 cloves garlic, minced",
            "1 teaspoon cornstarch",
            "1/4 cup chicken broth"
        ],
        [
            "Marinate chicken slices in soy sauce for 10 minutes.",
            "Heat sesame oil in a large pan or wok over high heat.",
            "Add chicken and stir-fry until cooked through, then remove from pan.",
            "Add garlic, bell pepper, carrot, and onion to the pan and stir-fry for 3-4 minutes.",
            "Return chicken to the pan.",
            "Mix cornstarch with chicken broth and pour into the pan.",
            "Cook until sauce thickens and everything is well coated.",
            "Serve immediately."
        ],
        "\nMedium 😤"
    ),
    Recipe(
        "Beef Wellington",
        [
            "1.5 lb beef tenderloin",
            "Salt and pepper to taste",
            "2 tablespoons olive oil",
            "2 tablespoons Dijon mustard",
            "8 oz mushrooms, finely chopped",
            "1 onion, finely chopped",
            "2 cloves garlic, minced",
            "1/4 cup white wine",
            "6 slices prosciutto",
            "1 sheet puff pastry",
            "1 egg, beaten"
        ],
        [
            "Preheat oven to 400°F (200°C). Season the beef tenderloin with salt and pepper.",
            "Heat olive oil in a skillet over high heat and sear the beef on all sides until browned. Remove "
            "from heat and brush with Dijon mustard.",
            "In the same skillet, sauté mushrooms, onion, and garlic until soft. Add white wine and cook "
            "until liquid evaporates. Let cool.",
            "Lay out the prosciutto slices on a sheet of plastic wrap, overlapping slightly. Spread the "
            "mushroom mixture evenly over the prosciutto.",
            "Place the beef on top and roll it up tightly using the plastic wrap. Chill in the refrigerator "
            "for 15 minutes.",
            "Roll out the puff pastry on a lightly floured surface. Remove the beef from the plastic wrap and place it in the center of the pastry.",
            "Wrap the pastry around the beef, sealing the edges. Brush with beaten egg.",
            "Place the wrapped beef on a baking sheet and bake for 25-30 minutes, or until the pastry is "
            "golden brown and the beef reaches your desired level of doneness.",
            "Let rest for 10 minutes before slicing and serving.",
        ],
        "\nDifficult 🤯"
    )
]


# Shows available recipes:
def show_available_recipes():
    print("\nAvailable recipes:")
    for index, recipe in enumerate(recipes, 1):
        print(f"{index}. {recipe.name}")


# Shows a specific recipe info:
def show_recipe_info(option):
    print("\nRecipe information:")
    recipes[option].show_info()


# Main function:
def main():
    while True:
        show_available_recipes()
        user_option = input("\nSelect the number of the recipe you want to view "
                            "or type 'exit' to close the app: ")

        if user_option.lower() == 'exit':
            print("\nThanks for using the app")
            print("Happy cooking! 😋🍽️")
            break
        else:
            try:
                option = int(user_option) - 1
                if 0 <= option < len(recipes):
                    show_recipe_info(option)
                else:
                    print("\nSorry, incorrect number. Please try again.")
            except ValueError:
                print("\nSorry, invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
