class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        n = len(nums)
        def per(i):
            if len(curr) >= n:
                ans.append(curr[:])
                return 
            
            for i in range(n):
                if nums[i] in curr:
                    continue
                curr.append(nums[i])
                per(i+1)
                curr.pop()

        per(0)
        return ans