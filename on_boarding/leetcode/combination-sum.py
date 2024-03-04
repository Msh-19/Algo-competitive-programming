class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        buck = []
        ans = []

        def backtrack(i):
            if target == sum(buck):
                ans.append(buck[:])
                return

            if target < sum(buck):
                return
            
            for j in range(i,len(candidates)):
                buck.append( candidates[j] )
                backtrack(j)
                buck.pop()       
        
        backtrack(0)
        return ans