class Solution:
    def numberOfWays(self, s: str) -> int:
        combo = 0
        onecount = zerocount = n01 = n10 = 0

        for n in s:
            if n == "0":
                zerocount += 1
                n10 += onecount
                combo += n01
            else:
                onecount += 1
                n01 += zerocount
                combo += n10

        return combo