class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = -1, len(letters)
        n = len(letters)
        temp = 0

        while left+1 < right:
            mid = (left + right)//2
            if letters[mid] > target:
                temp = mid
                right = mid
            else:
                left = mid 
        return letters[temp]