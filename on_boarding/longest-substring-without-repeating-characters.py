"""
[abcabcbb]
    b
 p
"""

class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        right, left = 0, 0
        stringSet = set()
        max_length = 0
        while right < len(s):
            if s[right] not in stringSet:
                stringSet.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                if s[left] in stringSet:
                    stringSet.remove(s[left])
                left += 1
        return max_length