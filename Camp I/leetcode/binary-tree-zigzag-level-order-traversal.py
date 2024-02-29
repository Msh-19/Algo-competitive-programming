# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level = 0
        def traverse(node,level):
            nonlocal result
            if not node:
                return

            if len(result) <= level:
                result.append(deque())

            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].appendleft(node.val)

            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, level)
        return result