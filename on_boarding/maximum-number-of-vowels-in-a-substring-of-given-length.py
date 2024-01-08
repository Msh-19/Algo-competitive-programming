class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_count = 0
        count = 0
        left = 0

        for right in range(len(s)):
            if s[right] in vowels:
                count += 1

            if right - left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                left += 1

            if right - left + 1 == k:
                max_count = max(max_count, count)

        return max_count