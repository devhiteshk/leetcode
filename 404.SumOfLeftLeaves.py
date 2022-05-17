# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
import queue as q
    
class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        else:
            ans = 0
            myQueue = q.Queue()
            myQueue.put(root)
            while not(myQueue.empty()):
                root = myQueue.get()
                
                try:
                    if root.left.left is None and root.left.right is None:
                        print(root.left.val)
                        ans += root.left.val
                        
                except:
                    pass
                
                if root.left is not None:
                    myQueue.put(root.left)
                if root.right is not None:
                    myQueue.put(root.right)
            return ans
            