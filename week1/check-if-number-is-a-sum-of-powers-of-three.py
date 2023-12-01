class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for p in range(14,-1,-1):
            if n//(3**p) == 2:
                return False
            n = n%3**p 
        return True