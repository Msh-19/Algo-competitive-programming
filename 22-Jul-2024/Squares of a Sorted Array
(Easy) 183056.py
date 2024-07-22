# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, n: List[int]) -> List[int]:
        return sorted(i*i for i in n)