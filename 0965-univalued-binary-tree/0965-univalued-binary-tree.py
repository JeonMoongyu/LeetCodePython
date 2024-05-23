# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        curr = True
        if root.left is not None:
            if root.right is not None:
                curr = (root.val == root.left.val and root.val == root.right.val)
            else:
                curr = root.val == root.left.val
        else:
            if root.right is not None:
                curr = root.val == root.right.val
        return curr and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)