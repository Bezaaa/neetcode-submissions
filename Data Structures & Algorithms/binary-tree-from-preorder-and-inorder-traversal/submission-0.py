# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # The first element of preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the root index in inorder
        index = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(preorder[1:1+index], inorder[:index])
        root.right = self.buildTree(preorder[1+index:], inorder[index+1:])

        return root


       


        