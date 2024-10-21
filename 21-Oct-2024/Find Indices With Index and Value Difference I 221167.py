# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        ptr1 = 0
        ptr2 = indexDifference

        if indexDifference == 0 and valueDifference == 0:
            return [0,0]

        for ptr1 in range(n-1):
            for ptr2 in range(ptr1+1,n):
                print(ptr1,ptr2)
                if abs(nums[ptr2]-nums[ptr1]) >= valueDifference and abs(ptr2 - ptr1) >= indexDifference:
                    return [ptr1,ptr2]
            
                
            
        return [-1,-1]