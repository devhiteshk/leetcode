# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root):
    if root is None:
        return 0
    else:
        leftDepth = maxDepth(root.left)
        rightDepth = maxDepth(root.right)
        
        if (leftDepth>rightDepth):
            return leftDepth + 1
        else:
            return rightDepth + 1

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(maxDepth(root.left),maxDepth(root.right)) + 1
                