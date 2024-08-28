# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0]*26

        for c in word:
            freq[ord(c)  - ord("a")] += 1

        freq.sort(reverse= True)

        totPushes = 0

        for i in range(26):
            if freq[i] ==0:
                break
            totPushes += (i//8+1)*freq[i]

        return totPushes

