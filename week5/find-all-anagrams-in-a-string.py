class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])

        if s_counter == p_counter:
            result.append(0)

        for i in range(len(p), len(s)):
            if s_counter[s[i - len(p)]] == 1:
                del s_counter[s[i - len(p)]]
            else:
                s_counter[s[i - len(p)]] -= 1

            s_counter[s[i]] += 1

            if s_counter == p_counter:
                result.append(i - len(p) + 1)
        return result