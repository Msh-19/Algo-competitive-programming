class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = str(x)[::-1]
        if x<0:
            return False
        if x == int(reversed):
            return True
        else:
            return False