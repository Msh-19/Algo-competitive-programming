# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        pt1 = 0
        pt2 = 0
        while pt1 < len(s) and pt2 < len(t):
            if s[pt1] == t[pt2]:
                pt1+=1
                if pt1 == len(s):
                    return True
            pt2+=1
        return False