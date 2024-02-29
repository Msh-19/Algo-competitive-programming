# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node, val):
            if not node:
                return node
            if val < node.val:
                node.left = delete(node.left, val)
            elif val > node.val:
                node.right = delete(node.right, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                temp = minval(node.right)
                node.val = temp.val

                node.right = delete(node.right,temp.val)
            return node
        def minval(node):
            current = node

            while current.left:
                current = current.left
            return current

        return delete(root, key)