# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowest(node, p,q):

            if node.val < p.val and node.val < q.val:
                return lowest(node.right, p , q)
            elif node.val > p.val and node.val > q.val:
                return lowest(node.left, p , q)
            else:
                return node
        return lowest(root,p,q)