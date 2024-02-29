# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversepath = [] 
        def findk(node):
            if not node:
                return
            findk(node.left)
            traversepath.append(node.val)
            findk(node.right)
        findk(root)
        return traversepath[k-1]