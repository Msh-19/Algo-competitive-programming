class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currS = 0
        output = 0
        prefixSums = { 0 : 1}
        for n in nums:
            currS += n
            diff = currS - k

            output += prefixSums.get(diff, 0)
            prefixSums[currS] = 1 + prefixSums.get(currS,0) 
        return output