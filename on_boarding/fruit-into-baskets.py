class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        store = {}

        start = 0
        for fruit in fruits:
            store[fruit] = store.get(fruit, 0) + 1

            if len(store)>2:
                store[fruits[start]] -= 1
                if store[fruits[start]] == 0:
                    del store[fruits[start]]
                start += 1
        return len(fruits) - start