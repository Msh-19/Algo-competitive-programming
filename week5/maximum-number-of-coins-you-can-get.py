class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        pos = 1
        answer = 0
        for i in range(len(piles)// 3):
            answer += piles[pos]
            pos += 2
        return answer