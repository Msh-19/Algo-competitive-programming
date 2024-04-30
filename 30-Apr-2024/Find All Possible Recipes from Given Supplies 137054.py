# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(list)

        for recipie, ingredient in zip(recipes,ingredients):
            indegree[recipie] = len(ingredient)

            for ing in ingredient:
                graph[ing].append(recipie)

        ans = []

        queue = deque(supplies)
        recipes = set(recipes)

        while queue:
            supply = queue.popleft()

            if supply in recipes:
                ans.append(supply)

            for recipie in graph[supply]:
                indegree[recipie] -= 1

                if indegree[recipie] == 0:
                    queue.append(recipie)

        return ans