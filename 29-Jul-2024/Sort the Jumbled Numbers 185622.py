# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for i in range(len(nums)):
            number = str(nums[i])
            form = ""

            for j in range(len(number)):
                form = form + str(mapping[int(number[j])])
            
            mapped = int(form)

            pairs.append((mapped,i))

        pairs.sort()

        answer = []

        for pair in pairs:
            answer.append(nums[pair[1]])
        return answer