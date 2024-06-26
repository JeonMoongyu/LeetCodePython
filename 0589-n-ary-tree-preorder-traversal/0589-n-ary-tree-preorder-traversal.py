"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        out = []
        
        def helper(node):
            if not node:
                return
            out.append(node.val)
            for child in node.children:
                helper(child)
        
        helper(root)
        return out