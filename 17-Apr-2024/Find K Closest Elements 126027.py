# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        for i in range(len(arr)):
            diff.append((abs(x-arr[i]),arr[i]))

        heapify(diff)
        res = []
        for i in range(k):
            res.append(heappop(diff)[1])
        res.sort()
        return res