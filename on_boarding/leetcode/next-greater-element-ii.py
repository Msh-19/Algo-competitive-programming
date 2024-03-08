class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        output = [-1]*len(nums)
        stack = []


        for i in range(2*len(nums)):
            i%=len(nums)

            while stack and nums[i] > nums[stack[-1]]:
                
                idx = stack.pop()
                output[idx] = nums[i]

            stack.append(i)

        return output