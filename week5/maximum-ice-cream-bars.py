class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        total_cost = 0
    
        for i in costs:
            total_cost += i
            if total_cost <= coins:  
                count += 1
            else:
                break
        return count