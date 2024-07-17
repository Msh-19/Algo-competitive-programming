# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleteset = set(to_delete)

        forest = []

        def dfs(node, is_root):
            if not node:
                return

            is_delete = node.val in deleteset

            if is_root and not is_delete:
                forest.append(node)

            node.left = dfs(node.left, is_delete)
            node.right = dfs(node.right,is_delete)

            return None if is_delete else node

        dfs(root,True)
        return forest