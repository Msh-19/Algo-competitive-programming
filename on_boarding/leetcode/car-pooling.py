class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_location = max(end for _, _, end in trips)
    
        passenger_changes = [0] * (max_location + 1)
        
        
        for passengers, start, end in trips:
            passenger_changes[start] += passengers
            passenger_changes[end] -= passengers
        
        
        current_passengers = 0
        for i in range(max_location + 1):
            current_passengers += passenger_changes[i]
            if current_passengers > capacity:
                return False
        
        return True