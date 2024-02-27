class Solution:
    def decodeString(self, s: str) -> str:
         
        l = len(s)
        output = ""
        i = 0
        while i < l:
            if s[i].isdigit():
                count = 0
                while s[i].isdigit():
                    count = count*10 + int(s[i])
                    i +=1 
                i += 1
                b = ""
                left = 1
                while i<l and left > 0:
                    if s[i] == "]":
                        left -= 1
                    elif s[i] == "[":
                        left += 1
                    if left > 0:
                        b += s[i] 
                    i += 1
                output += count*self.decodeString(b)
            else:
                output += s[i]
                i+=1

        return output