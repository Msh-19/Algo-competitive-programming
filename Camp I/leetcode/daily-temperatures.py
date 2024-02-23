class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monostack = []
        li = temperatures
        rt = [0]*len(li)
        for i in range(len(temperatures)):
            while monostack and li[i] > monostack[-1][1]:
                j,v = monostack.pop()
                rt[j] = (i-j)
            monostack.append((i,li[i]))

        return rt