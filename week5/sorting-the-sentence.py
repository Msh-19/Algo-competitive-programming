class Solution:
    def sortSentence(self, s: str) -> str:
        li = list(s.split())
        n = len(li)
        li2 = [0]*n
        for i in range(n):
            a = int(li[i][-1])
            li2[a-1] = li[i][0:-1]

        return " ".join(li2)