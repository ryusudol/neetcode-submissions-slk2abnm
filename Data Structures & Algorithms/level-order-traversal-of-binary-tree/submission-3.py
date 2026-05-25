# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([(0, root)])
        collector = []

        while queue:
            cur_level, node = queue.popleft()

            if len(res) < cur_level:
                res.append(collector.copy())
                collector.clear()
            
            collector.append(node.val)

            if node.left:
                queue.append((cur_level + 1, node.left))
            if node.right:
                queue.append((cur_level + 1, node.right))

        res.append(collector.copy())
        return res