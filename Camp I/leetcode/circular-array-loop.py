class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        checked =set()
        for i in range(n):
            if i not in checked:
                cycle_set =set()
                while True:
                    if i in cycle_set:
                        return True
                    checked.add(i)
                    cycle_set.add(i)
                    prev, i = i,(i+nums[i])%n

                    if prev == i:
                        break
                    if nums[prev]>0 != nums[i]<0:
                        break

        return False