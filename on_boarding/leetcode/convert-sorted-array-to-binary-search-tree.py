# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def builder(left, right):
            if left > right:
                return None

            mid = (left + right) // 2  
            node = TreeNode(nums[mid])  

            node.left = builder(left, mid - 1)
            node.right = builder(mid + 1, right)

            return node

        return builder(0, len(nums) - 1)