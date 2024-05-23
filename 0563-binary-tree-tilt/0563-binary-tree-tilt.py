# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return abs(self.sumTreeValues(root.left)-self.sumTreeValues(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
        
    def sumTreeValues(self, root):
        if root is None:
            return 0
        return root.val + self.sumTreeValues(root.left) + self.sumTreeValues(root.right)