# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        Q = deque([root])
        out = 2 ** 31
        rootVal = root.val
        while Q:
            node = Q.popleft()
            if rootVal < node.val and node.val < out:
                out = node.val
            if node.left is not None:
                Q.append(node.left)
                Q.append(node.right)
        return -1 if out == 2 ** 31 else out