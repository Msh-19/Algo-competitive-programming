class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
        def backtrack(idx):
            if len(nums) <= idx:
                if not curr in res:
                    res.append(curr[:])
                return
            curr.append(nums[idx])
            backtrack(idx+1)
            curr.pop() 
            backtrack(idx+1)

        backtrack(0)
        return res