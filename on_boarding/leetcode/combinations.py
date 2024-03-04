class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curr = []
        
        def com(idx):
            if idx > n:
                return
            
            if len(curr) >= k:
                ans.append(curr[:])
                return 
            
            curr.append(idx+1)
            com(idx+1)
            curr.pop()
            com(idx+1)

        com(0)
        return ans
            