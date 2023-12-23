class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        total = sum(nums)

        best = total
        score = total
        ans = [0]

        for left in range(N):
            if nums[left] == 0:
                score += 2
            else:
                score -= 2
            
            if best == score:
                ans.append(left + 1)
            elif best < score:
                best = score
                ans = [left + 1]
        return ans