# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):   
        if not node: 
            return 0
        lft = self.dfs(node.left) 
        rgh = self.dfs(node.right)

        if abs(lft - rgh) > 1: 
            self.Bal = False
        return max(lft, rgh) + 1
    
    def isBalanced(self, root) -> bool:
            self.Bal = True
            self.dfs(root)
            return self.Bal