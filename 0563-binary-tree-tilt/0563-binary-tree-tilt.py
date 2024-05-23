# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        out = 0
        
        def sumTree(node):
            nonlocal out
            
            if node is None:
                return 0
            sumLeft = sumTree(node.left)
            sumRight = sumTree(node.right)
            tilt = abs(sumLeft - sumRight)
            out += tilt
            
            return node.val + sumLeft + sumRight
        
        sumTree(root)
        return out
        