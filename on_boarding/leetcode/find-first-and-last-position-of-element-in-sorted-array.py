class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = -1
        right = len(nums)
        flag = False

        while left+1 < right:
            mid = (left + right)//2
            if nums[mid] == target:
                flag = True
            if nums[mid] >= target :
                right = mid
            else:
                left = mid 
        
        inter1 = right


        left = -1
        right = len(nums)
        while left+1 < right:
            mid = (left + right)//2
            if nums[mid] <= target :
                left = mid
            else:
                right = mid 
        
        inter2 = left
        print(inter1,inter2)
        if flag == True:
            return [inter1, inter2]

        return [-1,-1]