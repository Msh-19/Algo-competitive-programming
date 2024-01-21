class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        tar = float("inf")
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                print(sum3)
                if sum3 < target:
                    l += 1
                else:
                    r -= 1
                if abs(sum3 - target) < abs(tar - target):
                    tar = sum3
        return tar
