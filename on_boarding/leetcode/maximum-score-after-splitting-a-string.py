class Solution(object):
    def maxScore(self, s):
        result = 0
        for i in range(len(s) - 1):
            current_score = 0
            for j in range(i + 1):
                if s[j] == '0':
                    current_score += 1
            for j in range(i + 1, len(s)):
                if s[j] == '1':
                    current_score += 1
            result = max(result, current_score)
        return result