# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums is None:
            return None

        val = max(nums)
        idx = nums.index(val)
        
        node = TreeNode(val)

        if len(nums[:idx]):
            node.left = self.constructMaximumBinaryTree(nums[:idx])

        if len(nums[idx+1:]):
            node.right = self.constructMaximumBinaryTree(nums[idx+1:])

        return node