# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        z=x^y

        while z!=0:
            if z&1 == 1:
                count +=1 
            z>>=1

        return count