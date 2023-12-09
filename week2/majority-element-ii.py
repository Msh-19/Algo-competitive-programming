class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        output = []
        
        for num in set(nums):
            if nums.count(num) > threshold:
                output.append(num)
        
        return output