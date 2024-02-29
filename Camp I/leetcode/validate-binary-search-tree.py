# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        state = True
        maxval = inf
        minval = -inf
        
        def validate(node):
            nonlocal maxval, minval, state
            if not node:
                return 

            if node.val >= maxval or node.val <= minval:
                state = False
                return state
            # for each subtree

            #for left subtree
            temp = maxval
            maxval = node.val
            validate(node.left)

            #for right subtree
            maxval = temp
            minval = node.val
            validate(node.right)


        validate(root)
        return state
