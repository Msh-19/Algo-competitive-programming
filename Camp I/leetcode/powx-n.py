class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
                return 0
        if n > 0:
            if n%2 != 0:
                return x*self.myPow(x,(n-1))
            else:
                return self.myPow(x*x,(n//2))
            
        if n == 0:
            return 1

        elif n < 0:
            return 1/self.myPow(x,(-n))
            
