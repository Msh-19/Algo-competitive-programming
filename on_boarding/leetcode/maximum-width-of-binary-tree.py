# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mat = {}
        width = -inf
        def check(node,row,col):
            if not node:
                return 

            if row in mat:
                mat[row][0] = min(mat[row][0], col)
                mat[row][1] = max(mat[row][1], col)
            else:
                mat[row] = [col,col]

            check(node.left,row+1,2*col)
            check(node.right,row+1,2*col+1)

        check(root,0,0)
        for i,j in mat.values():
            width = max(width,j-i+1)
        return width