# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(node):
            if not node:
                return 
            if not node.children:
                res.append(node.val)
            else:
                for i in node.children:
                    helper(i)
                res.append(node.val)

        helper(root)
        return res