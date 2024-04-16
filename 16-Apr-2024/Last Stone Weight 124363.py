# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*-1 for i in stones]
        heapify(stones)
        
        while len(stones) >= 2:
            y = -heappop(stones)
            x = -heappop(stones)
            z = abs(y-x)
            if z!=0:
                heappush(stones,-z)
        if len(stones) == 1:
            return -stones[0]

        return 0