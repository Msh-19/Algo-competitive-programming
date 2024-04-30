# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_ = int(a,2) + int(b,2)
        sum_ = bin(sum_)[2:]
        return sum_