class RecentCounter:

    def __init__(self):
        self.dequeue = Deque()
        

    def ping(self, t: int) -> int: 
        
        while self.dequeue and self.dequeue[0] < t - 3000:
            self.dequeue.popleft()

        self.dequeue.append(t)
        return len(self.dequeue)    
        

    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)