# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            
            total = 0
            if grandparent % 2 == 0:
                total += node.val
            
            total += dfs(node.left, node.val, parent)
            total += dfs(node.right, node.val, parent)
            return total
        return dfs(root,-1,-1)