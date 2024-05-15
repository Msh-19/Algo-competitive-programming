# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(i,j):
            if i<len(text1) and j<len(text2):
                if (text1[i] == text2[j]):
                    if (i,j) in memo:
                        return memo[(i,j)]
                    else:
                        memo[(i,j)] = dp(i+1,j+1) + 1 
                        return memo[(i,j)]
                else:
                    if (i,j) not in memo:
                        memo[(i,j)] = max(dp(i+1,j),dp(i,j+1))
                        return memo[(i,j)]
                    else:
                        return memo[(i,j)]
            else:
                return 0
        return dp(0,0)