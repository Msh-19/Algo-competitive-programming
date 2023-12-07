class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new = []
        half_index = len(nums)//2
        for i in range(len(nums)//2):
            new.append(nums[i])
            new.append(nums[i + half_index])
        return new