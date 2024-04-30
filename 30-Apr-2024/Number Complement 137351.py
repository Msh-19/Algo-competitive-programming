# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num)[2:]
        val = (1<<len(n)) - 1

        return val^num