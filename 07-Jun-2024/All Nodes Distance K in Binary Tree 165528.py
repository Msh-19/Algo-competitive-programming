# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_dict = defaultdict(list)
        queue = deque([root])

        while queue:
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
                node_dict[node.val].append(node.left.val)
                node_dict[node.left.val].append(node.val)
            if node.right:
                queue.append(node.right)
                node_dict[node.val].append(node.right.val)
                node_dict[node.right.val].append(node.val)

        ans = []
        que = deque([(target.val,0)])
        visited = set([target.val])

        while que:
            num,level = que.popleft()
            if level == k:
                ans.append(num)
            for n in node_dict[num]:
                if n not in visited:
                    que.append([n,level + 1])
                    visited.add(n)

        return ans
