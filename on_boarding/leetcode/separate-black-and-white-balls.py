class Solution:
    def minimumSteps(self, s: str) -> int:
        output = 0
        swaps = 0

        for letter in s:
            if letter == "1":
                swaps += 1
            else:
                output += swaps
        return output
            

