# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product  = 1
        for num in nums:
            product *= num

        prime_factors = set()
        divisor = 2
        while product > 1:
            while product % divisor == 0:
                prime_factors.add(divisor)
                product //= divisor

            divisor += 1

        return len(prime_factors)