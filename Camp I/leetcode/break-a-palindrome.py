class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return ""
        li = list(s)
        dic = Counter(s)
        flag = True
        for i in range(len(li)//2):
           if li[i] != "a":
               li[i] = "a"
               flag = False
               break
        if flag == True:
            for i in range(len(li)-1, (len(li) -1)//2 , -1):
                if li[i]!= "b":
                    li[i] = "b"
                    flag = False
                    break
        if flag == True:
            return ""
        else:
            return "".join(li)

            
                