class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum(x for x in nums if x%2 == 0)
        res = []

        for val, index in queries:
            prev_num = nums[index]
            nums[index] += val

            if prev_num%2 == 0:
                evenSum -= prev_num

            if nums[index]%2 == 0:
                evenSum += nums[index]

            res.append(evenSum)

        return res