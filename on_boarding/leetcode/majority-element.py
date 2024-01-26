class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxed = 0
        majority = 0

        for num,frequency in count.items():
            if frequency > maxed:
                maxed = frequency
                majority = num


        return majority