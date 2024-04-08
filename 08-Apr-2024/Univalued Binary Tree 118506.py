# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()

        q.append(root)
        qval = q[-1].val

        while q:
            cur = q.pop()
            if cur.left:
                if cur.left.val != qval:
                    return False
            
                q.appendleft(cur.left)

            if cur.right:
                if cur.right.val != qval:
                    return False
                q.appendleft(cur.right)
                
        return True

            

