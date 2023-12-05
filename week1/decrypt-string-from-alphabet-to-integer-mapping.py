class Solution:
    def freqAlphabets(self, s: str) -> str:
        map = {}
        for i in range(1,27):
            if i<=9:
                map[str(i)] = chr(i + ord("a") - 1)
            else:
                map[str(i) +'#'] = chr(i + ord("a") - 1)

        result = []
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                result.append(map[s[i:i+3]])
                i+=3
            else:
                result.append(map[s[i]])
                i+=1

        return "".join(result)