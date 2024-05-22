# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        dp = [[] for _ in range(N)]
        dp[0].append([s[0]])
        # print(dp)
        for i in range(1, N):
            for j in range(i, 0, -1):
                t = s[j:i + 1]
                if t == t[::-1]:
                    for a in dp[j - 1]:
                        dp[i].append(a + [t])
                # print(i, j, dp)
            t = s[:i + 1]
            if t == t[::-1]:
                dp[i].append([t])
        # print(dp)
        return dp[N - 1]