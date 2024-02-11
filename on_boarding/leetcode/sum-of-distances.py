class Solution:
    def distance(self, nums: List[int]) -> List[int]: 
        mp=defaultdict(list)
        for i,j in enumerate(nums):
            mp[j].append(i)
        
        ans=[0]*len(nums)
        for key,val in mp.items():
            suffixSum = sum(val)
            prefixSum = 0
            suffixLength = len(val)
            prefixLength=0
            for i in val:
                prefixSum += i 
                prefixLength += 1
                suffixSum -= i
                suffixLength -= 1
                ans[i] = (-prefixSum + prefixLength*i - suffixLength*i + suffixSum) 
        return ans