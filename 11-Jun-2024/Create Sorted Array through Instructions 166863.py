# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(instructions)
        less = [0] * n
        greater = [0] * n

        def getCounts(arr, left, right):
            if left >= right:
                return
            
            mid = (left + right) // 2
            getCounts(arr, left, mid)
            getCounts(arr, mid + 1, right)

            copy = arr[left:mid+1]
            copy.sort()

            for i in range(mid + 1, right + 1):
                smaller = bisect_left(copy, arr[i])
                larger = len(copy) - bisect_right(copy, arr[i])

                less[i] += smaller
                greater[i] += larger
        
        getCounts(instructions, 0, n - 1)
        
        cost = 0
        for smaller, larger in zip(less, greater):
            cost = (cost + min(smaller, larger)) % mod
        
        return cost