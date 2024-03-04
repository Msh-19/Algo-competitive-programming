class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(idx):
            if len(nums) <= idx:
                res.append(curr[:])
                return
            
            curr.append(nums[idx])
            backtrack(idx+1)
            curr.pop() 
            backtrack(idx+1)

        backtrack(0)
        return res