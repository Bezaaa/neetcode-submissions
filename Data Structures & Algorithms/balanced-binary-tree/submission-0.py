# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_height(self , root):
            if root is None:  
              return 0
            left = self.check_height(root.left)
            right = self.check_height(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1: 
                return -1
            return max(left, right) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_height(root)>=0