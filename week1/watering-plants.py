class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i = 0
        step = 0
        cap = capacity
        while i<len(plants):
            if cap >= plants[i]:
                cap -= plants[i]
                step += 1
                i += 1

            else:
                cap = capacity
                step += i*2

        return step