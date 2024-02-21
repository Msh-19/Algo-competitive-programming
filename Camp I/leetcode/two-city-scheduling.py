class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        A = len(costs)/2
        B = len(costs)/2
        costs.sort(key = lambda x: abs(x[0] - x[1]), reverse=True)
        total = 0
        for acost, bcost in costs:
            if B == 0 or (A>0 and acost <= bcost):
                total += acost
                A -= 1
            else: 
                total += bcost
                B -= 1 

        return total