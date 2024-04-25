# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        par = {i:i for i in 'abcdefghijklmnopqrstuvwxyz'}
        
        def find(x):
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]

        def union(x,y):
            px = find(x)
            py = find(y)
            if px == py:
                return px
            else:
                if ord(px) > ord(py):
                    par[px] = py
                elif ord(px) < ord(py):
                    par[py] = px


        n = len(s1)
        for i in range(n):
            union(s1[i],s2[i])
        

        ans = ""
        for ch in baseStr:
            ans += find(ch)

        return ans