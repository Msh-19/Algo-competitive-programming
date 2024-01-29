class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        n = len(s) // 4
        extras = {}

        for key in counter:
            if counter[key] > n:
                extras[key] = counter[key] - n

        if not extras:
            return 0

        i = 0
        output = len(s)

        for j in range(len(s)):
            if s[j] in extras:
                extras[s[j]] -= 1

            while max(extras.values()) <= 0:
                output = min(output, j - i + 1)

                if s[i] in extras:
                    extras[s[i]] += 1

                i += 1

        return output