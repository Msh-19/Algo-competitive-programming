class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count = 0
        i = 0
        j = 0
        while i < len(s) and j < len(g):
            if s[i] - g[j] >= 0:
                count += 1
                i+=1
                j+=1
            else:
                i+=1 
        return count