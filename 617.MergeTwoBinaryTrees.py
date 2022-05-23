# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1,t2):
        
        # By using Recursion
        
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # t = TreeNode(root1.val+root2.val)
        # t.left = self.mergeTrees(root1.left,root2.left)
        # t.right = self.mergeTrees(root1.right, root2.right)
        # return t
        
        # By using iteration and stack
        
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # if t1 is an empty tree
        if t1 is None:
            return t2
        
        # init stack
        stack = []
        
        stack.append((t1,t2))
        
        while stack:
            t = stack.pop()
            
            # check if second node is None, if that's the case, directly pop the next element
            if t[1] is None:
                continue
                
            t[0].val += t[1].val
            
            # push left child of two input nodes to stack
            # if left child of first node is None, directly assign value of left child of second node
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left,t[1].left))
            
            # push right child of two input nodes to stack
            # if right child of first node is None, directly assign value of right child of second node
            
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right,t[1].right))
        return t1