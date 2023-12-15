class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        offset = 0
        for pos in spaces:
            if pos+offset <= len(s):
                s = s[:pos+offset] + ' ' + s[pos+offset:]
                offset+=1
        return s