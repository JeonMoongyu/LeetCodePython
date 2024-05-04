# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)
    def helper(self, root, targetSum, prevSum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val + prevSum == targetSum
        prevSum += root.val
        return self.helper(root.left, targetSum, prevSum) or self.helper(root.right, targetSum, prevSum)