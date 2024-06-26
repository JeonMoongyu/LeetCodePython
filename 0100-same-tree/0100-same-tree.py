# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            if p == None and q == None:
                return True
            else:
                return False
        return self.isSameTree(p.left, q.left) and p.val == q.val and self.isSameTree(p.right, q.right)