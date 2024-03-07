class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        valid = True

        for i in range(len(s)):
            if ord(s[i]) > 95 and s[i].upper() in s:
                continue
            elif ord(s[i]) < 95 and s[i].lower() in s:
                continue
            else:
                valid = False
                break

        if valid:
            return s
        else:
            right = self.longestNiceSubstring(s[:i])
            left = self.longestNiceSubstring(s[i+1:])

            if len(left) <= len(right):
                return right
            else:
                return left