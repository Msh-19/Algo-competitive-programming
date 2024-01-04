class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        count = 0 

        while left<right:
            if people[left] + people[right] <= limit:
                count +=1
                left += 1
                right -= 1
            else: 
                right -= 1
        return len(people) - count