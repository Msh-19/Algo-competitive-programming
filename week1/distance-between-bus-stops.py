class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
             start, destination = destination, start   
        return min(sum(distance[start:destination]), (sum(distance[0:start])+sum(distance[destination:len(distance)])))
 # need serious revision 