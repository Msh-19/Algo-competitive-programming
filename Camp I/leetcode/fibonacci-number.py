class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n

        number = self.fib(n-1) + self.fib(n-2)
        return number