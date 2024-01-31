class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        count = {}

        start = 0

        for end in range(len(s)):
            char = s[end]
            count[char] = count.get(char, 0) + 1
            max_count = max(max_count, count[char])

            
            replace = (end - start + 1) - max_count

            
            if replace > k:
                count[s[start]] -= 1
                start += 1

            
            max_len = max(max_len, end - start + 1)

        return max_len
