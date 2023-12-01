class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num//3
        array = [x-1,x,x+1]
        sumArray = 0
        for x in array:
            sumArray = sum(array)
        if sumArray == num:
            return array
        else:
            return []
        