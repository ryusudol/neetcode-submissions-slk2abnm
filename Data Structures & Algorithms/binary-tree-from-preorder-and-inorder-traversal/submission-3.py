# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(n)
        inorder_idx = { val: idx for idx, val in enumerate(inorder) }
        self.pre_idx = 0

        def dfs(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)
            mid = inorder_idx[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root
        
        return dfs(0, len(inorder) - 1)

        # O(n^2)
        # if not inorder:
        #     return None

        # root_val = preorder.pop(0)
        # root_idx = inorder.index(root_val)

        # root = cur = TreeNode(root_val)
        # root.left = self.buildTree(preorder, inorder[:root_idx])
        # root.right = self.buildTree(preorder, inorder[root_idx + 1:])

        # return root