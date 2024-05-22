# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            if self.sameTree(node, subRoot):
                return True
        return False
    
    def sameTree(self, root1, root2):
        if root1 is None or root2 is None:
            if root1 is None and root2 is None:
                return True
            return False
        return root1.val == root2.val and self.sameTree(root1.left, root2.left) and \
               self.sameTree(root1.right, root2.right)
            