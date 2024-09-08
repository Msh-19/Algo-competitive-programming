# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumrolls = sum(rolls)

        remaining_sum = mean*(n+len(rolls)) - sumrolls

        if remaining_sum > 6* n or remaining_sum < n:
            return []
        distribute_mean = remaining_sum//n
        mod = remaining_sum % n
        n_elements = [distribute_mean]*n

        for i in range(mod):
            n_elements[i] += 1
        return n_elements