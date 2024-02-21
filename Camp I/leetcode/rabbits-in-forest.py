class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = Counter(answers)
        ans = 0
        for i, val in dic.items():
            ans += ceil(val/(i + 1))*(i + 1)

        return ans
