class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        dic = Counter(s)
        rt = 0
        flag = True

        for i in dic:
            if dic[i]%2 == 0:
                rt += dic[i]
            else:
                if dic[i]>2:
                    rt +=(dic[i] - 1)
                    

                if flag == True:
                    rt +=1
                    flag = False

        return rt 