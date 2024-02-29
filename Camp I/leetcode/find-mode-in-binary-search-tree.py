# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        counts = defaultdict(int)
        def traverse(node):
            if not node:
                return 
            
            counts[node.val]+= 1
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        maxcount = max(counts.values())
        result = []
        for num,count in counts.items():
            if count == maxcount:
                result.append(num)
        
        return result
