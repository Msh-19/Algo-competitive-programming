# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = 1
        j = 1
        
        for i in range(time):
            if j == n:
                p = -1
            if j == 1:
                p = 1

            j+=p

        return j