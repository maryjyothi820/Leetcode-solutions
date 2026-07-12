2115. Find All Possible Recipes from Given Supplies.py
from collections import deque, defaultdict

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):

        graph = defaultdict(list)

        # Count required ingredients for each recipe
        need = {}

        for i in range(len(recipes)):
            recipe = recipes[i]
            need[recipe] = len(ingredients[i])

            for ing in ingredients[i]:
                graph[ing].append(recipe)

        queue = deque(supplies)

        ans = []
        available = set(supplies)

        while queue:

            item = queue.popleft()

            for recipe in graph[item]:

                need[recipe] -= 1

                # All ingredients available
                if need[recipe] == 0:

                    ans.append(recipe)

                    # Recipe becomes a supply
                    queue.append(recipe)

        return ans
