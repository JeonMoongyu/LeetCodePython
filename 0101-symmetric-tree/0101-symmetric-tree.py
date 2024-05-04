# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isReflective(root.left, root.right)
    def isReflective(self, p, q):
        if p == None or q == None:
            if p == None and q == None:
                return True
            else:
                return False
        if p.val != q.val:
            return False
        return self.isReflective(p.left, q.right) and self.isReflective(p.right, q.left)