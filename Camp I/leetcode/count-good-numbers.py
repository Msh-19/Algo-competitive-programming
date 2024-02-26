class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9)+7
        def myPow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return x
            if n > 0:
                if n%2 != 0:
                    return x*myPow(x,(n-1))%mod
                else:
                    return myPow(x*x%mod,(n//2))%mod
                
        if n == 1:
            return 5
        if n%2!= 0:
            return myPow(20,((n-1)//2)) * (5)%mod
        elif n%2 == 0:
            return myPow(20,((n//2)))