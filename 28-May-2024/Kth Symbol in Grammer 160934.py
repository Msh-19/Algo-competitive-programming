# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        left,right = 1,2**(n-1)
        curr = 0

        for i in range(n-1):
            mid = (left + right)//2

            if k <=mid:
                right = mid
            else:
                left = mid + 1
                curr = 0 if curr else 1 

        return curr
