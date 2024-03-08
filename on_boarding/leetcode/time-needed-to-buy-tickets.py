class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dequeue = deque(enumerate(tickets))
        seconds = 0
        while True:
            i,front = dequeue.popleft()
            seconds += 1
            if front >1:
                dequeue.append((i,front-1))
            elif i == k:
                return seconds
        
