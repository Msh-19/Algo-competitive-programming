# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        output = []
        if not root:
            return []
        q.append(root)
        level = 0
        visit = set()
        dic = defaultdict(list)
        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                dic[level].append(cur.val)
            level+=1
        
        for i,j in dic.items():
            output.append(j)

        return output

                     

