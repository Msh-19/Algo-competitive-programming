class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)

        left = 0
        right = len(s1)
        temp = Counter(s2[0:right])
        temp2 = Counter(s1)
        if temp == temp2:
            return True
        for i in range(right,len(s2)):
            temp[s2[left]] -=1
            if temp[s2[left]] == 0:
                del temp[s2[left]]
            temp[s2[i]] += 1

            left += 1

            if temp == temp2:
                return True

        return False