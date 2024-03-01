# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val) and symmetric(left.left,right.right) and symmetric(left.right,right.left)

        if not root:
            return True
        return symmetric(root.left,root.right)
