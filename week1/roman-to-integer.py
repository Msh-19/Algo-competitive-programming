class Solution:
    def romanToInt(self, s: str) -> int:
        
        collor = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and collor[s[i]] < collor[s[i+1]]:
                ans -= collor[s[i]]
            else:
                ans += collor[s[i]]
        return ans
                
                    