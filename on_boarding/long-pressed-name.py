class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False

            if not (i < len(name) - 1 and name[i] == name[i+1]) and j < len(typed) - 1 and  name[i] == typed[j+1]:
                j += 1
                continue
            i += 1
            j += 1   
            
        return i==len(name) and j==len(typed)