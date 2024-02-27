class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def deduction(li):
            if len(li) == 1:
                return li[0]
            if len(li) == 2:
                return max(li)
            
            first = li[0]
            r1 = li[1:-1]
            r2 = li[2:]
            v1 = first+min(deduction(r1),deduction(r2))

            second = li[-1]
            r1 = li[1:-1]
            r2 = li[:-2]
            v2 = second+min(deduction(r1), deduction(r2))

            player1 = max(v1,v2)

            return player1

        player1 = deduction(nums)
        player2 = sum(nums) - player1
        return  player1 >= player2 