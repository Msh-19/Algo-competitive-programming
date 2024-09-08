# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        
        while k > 0:
            num_str = str(sum(int(digit) for digit in num_str))
            k -= 1
        
        return int(num_str)

        