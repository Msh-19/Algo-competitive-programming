# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.li = []
        self.k = k
        for n in nums:
            heappush(self.li,n)
            if len(self.li) > k:
                heappop(self.li)


    def add(self, val: int) -> int:
        heappush(self.li,val)
        if len(self.li) > self.k:
            heappop(self.li)
        return self.li[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)