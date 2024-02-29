# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxnum = root.val
        minnum = root.val
        diff = 0
        maxdiff = 0
        def findMinAndMaxDiff(node,minnum,maxnum):
            nonlocal maxdiff
            if not node:
                return 
            
            maxnum = max(node.val,maxnum)
            minnum = min(node.val,minnum)

            diff = abs(maxnum - minnum)

            maxdiff = max(maxdiff, diff)

            findMinAndMaxDiff(node.left,minnum,maxnum)
            findMinAndMaxDiff(node.right,minnum,maxnum)
        findMinAndMaxDiff(root, minnum, maxnum)
        return maxdiff


            