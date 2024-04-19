# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        use = 0
        dif = []
        
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue

            heappush(dif,diff)
            if len(dif) >ladders:
                use += heappop(dif)
                if use > bricks:
                    return i
                    
        return len(heights)-1