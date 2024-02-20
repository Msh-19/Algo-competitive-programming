class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        NumOnes = [1]*numOnes
        NumZeros = [0]*numZeros
        NumNegOnes = [-1]*numNegOnes
        
        total = []
        total.extend(NumOnes)
        total.extend(NumZeros)
        total.extend(NumNegOnes)

        sumk = sum(total[:k])
        return sumk