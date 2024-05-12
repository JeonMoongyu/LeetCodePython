# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        Q1, Q2 = deque([original,]), deque([cloned,])
        
        while Q1:
            node1, node2 = Q1.popleft(), Q2.popleft()
            if node1 == target:
                return node2
            if node1.left:
                Q1.append(node1.left)
                Q2.append(node2.left)
            if node1.right:
                Q1.append(node1.right)
                Q2.append(node2.right)

            