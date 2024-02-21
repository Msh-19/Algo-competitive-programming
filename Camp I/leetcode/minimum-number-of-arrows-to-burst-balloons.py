class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        intersect = 0
        points.sort(key=lambda x: x[1])
        print(points)
        
        arrows = 1
        end = points[0][1]
        
        for i in range(1, len(points)):
            start, finish = points[i]

            if start > end:
                arrows += 1
                end = finish

            else:
                end = min(end, finish)

        return arrows




