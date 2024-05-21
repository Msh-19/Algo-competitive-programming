# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution(object):
    def mostPoints(self, questions):
        dp = [0]*(len(questions))
        dp[-1] = questions[-1][0]
        for i in range(len(questions)-2,-1,-1):
            points,n = questions[i]
            exclude = dp[i+1]
            include = points
            
            if i+(n+1) < len(questions):
                include = dp[i+n+1] + points
            dp[i] = max(include,exclude)

        return dp[0]