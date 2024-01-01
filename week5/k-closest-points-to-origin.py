import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p = [0,0]

        points.sort( key = lambda x: math.dist(p,x))

        return points[0:k]