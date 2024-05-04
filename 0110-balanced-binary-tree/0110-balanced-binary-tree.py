# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return np.abs( self.getHeight(root.left) - self.getHeight(root.right) ) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def getHeight(self, root):
        if root == None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))