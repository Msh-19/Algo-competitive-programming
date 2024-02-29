# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        currsum = 0
        fullSum = 0
        def retraverse(node):
            nonlocal currsum, fullSum
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                currsum = "".join(path)
                fullSum += int(currsum)
            

            retraverse(node.left)
            retraverse(node.right)
            path.pop()
        retraverse(root)
        return fullSum