# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()

        currav = []
        curval = 0

        q.append(root)
        if not root:
            return []
        while q:
            n = len(q)
            sum_ = 0
            for _ in range(n):
                cur = q.popleft()
                sum_ += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            currav.append(sum_ / n)

        return currav
