class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: return 0
        output = 0
        if num < 0:
            value = abs(num)
            li = list(str(value))
            li.sort(reverse = True)
            output = int("".join(li))
            return -output
        
        li = list(str(num))
        li.sort()
        if li[0] == "0":
            for i in range(len(li)):
                if li[i] != "0":
                    li[0], li[i] = li[i], li[0]
                    break
        output = int("".join(li))
        return output

