class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = [x for x in nums if x<0]
        positives = [x for x in nums if x>0]
        output = []
        for i in range(len(nums)//2):
            output.append(positives[i])
            output.append(negatives[i])
        return output