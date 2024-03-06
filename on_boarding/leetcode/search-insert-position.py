class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums) 

        temp = 0
        while left+1 < right:
            mid = (left + right)//2
            if nums[temp] == target:
                return temp 
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
            print(mid)

        return right
