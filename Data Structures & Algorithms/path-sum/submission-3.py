# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(node, cum) -> bool:
            if not node: return False

            cum += node.val

            if not node.left and not node.right:
                return cum == targetSum
            return backtrack(node.left, cum) or backtrack(node.right, cum)
        
        return backtrack(root, 0)