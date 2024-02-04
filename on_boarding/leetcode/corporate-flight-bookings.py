class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        reserved = [0] * (n + 1)
        for booking in bookings:
            first, last, seats = booking
            reserved[first - 1] += seats
            reserved[last] -= seats

        for i in range(1, n):
            reserved[i] += reserved[i - 1]

        return reserved[:-1]