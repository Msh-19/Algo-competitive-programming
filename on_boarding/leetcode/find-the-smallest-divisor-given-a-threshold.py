class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        n= len(nums)
        left = 0
        right = nums[-1] + 1
        def check(mid):
            div = mid
            val = 0
            li = []
            for i in range(n):
                if nums[i]%mid != 0:
                    val = nums[i]//mid + 1
                    li.append(val)
                else:
                    val = nums[i]//mid
                    li.append(val)
            if sum(li) > threshold:
                return False
            else:
                return True

        while left+1<right:
            mid = (left + right)// 2
            val = check(mid)
            if val:
                right = mid
            elif not val:
                left = mid
        
        return right
        