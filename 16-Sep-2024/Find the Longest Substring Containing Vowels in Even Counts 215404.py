# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0

        characterMap = [0] * 26
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

        for vowel, value in vowels.items():
            characterMap[ord(vowel) - ord('a')] = value
        mp = [-1] * 32 
        longestSubstr = 0

        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i])- ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
                
            longestSubstr = max(longestSubstr, i - mp[prefixXOR])
        return longestSubstr