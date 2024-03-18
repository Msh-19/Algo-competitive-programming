class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = Counter(s)
        countt = Counter(t)

        if counts == countt:
            return True
        else:
            return False