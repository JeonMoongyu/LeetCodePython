# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        Q = queue.Queue()
        Q.put(cloned)
        while not Q.empty():
            node = Q.get()
            if node.val == target.val:
                return node
            if node.left:
                Q.put(node.left)
            if node.right:
                Q.put(node.right)
            