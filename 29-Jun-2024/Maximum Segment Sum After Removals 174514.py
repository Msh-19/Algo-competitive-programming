# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class U:
    def __init__(self,n,nums):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.sum = nums

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        parX = self.find(x)
        parY = self.find(y)

        if parX != parY:
            if self.rank[parX] > self.rank[parY]:
                self.parent[parY] = parX 
                self.sum[parX] += self.sum[parY]
            elif self.rank[parY] > self.rank[parX]:
                self.parent[parX] = parY
                self.sum[parY] += self.sum[parX]
            else:
                self.parent[parY] = parX
                self.rank[parX] += 1
                self.sum[parX] += self.sum[parY]
    
    def connected(self, x,y):
        return self.find(x) == self.find(y)

class Solution:
    def maximumSegmentSum(self, nums: List[int], removals: List[int]) -> List[int]:
        n = len(nums)
        du = U(n,nums)
        res = [0 for _ in range(n)]
        maxSum = 0
        curr = [0]*n
        
        for i in range(n-1,-1,-1):
            res[i] = maxSum
            q = removals[i]
            if q-1 >= 0 and curr[q-1]>0:
                du.union(q,q-1)
            if q+1 <n and curr[q+1]>0:
                du.union(q,q+1)
                
            maxSum = max(maxSum,du.sum[du.find(q)])
            curr[q] = nums[q]

        return res
