class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        buck = []
        ans = []
        check = set()

        candidates.sort()
        print(candidates)

        def backtrack(i):
            if target == sum(buck):
                if tuple(buck) not in check:
                    ans.append(buck[:])
                    check.add(tuple(buck) )
                return

            if target < sum(buck):
                return
            val = None
            for j in range(i,len(candidates)):
                if val != candidates[j]:
                    buck.append( candidates[j] )
                    backtrack(j+1)
                    val = buck.pop()       
        
        backtrack(0)
        print(check)

        return ans