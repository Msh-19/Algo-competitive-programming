class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_indices = {num:i for i, num in enumerate(nums)}

        for old_num, new_num in operations:
            index = num_indices[old_num]
            nums[index] = new_num

            num_indices[new_num] = index
            del num_indices[old_num]

        return nums