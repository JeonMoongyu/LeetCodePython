# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node1, node2):
            if node1 is None and node2 is None:
                return None
            if node1 is None and node2 is not None:
                return node2
            elif node1 is not None and node2 is None:
                return node1
            out = TreeNode(node1.val + node2.val)
            out.left = helper(node1.left, node2.left)
            out.right = helper(node1.right, node2.right)
            return out
        
        return helper(root1, root2)