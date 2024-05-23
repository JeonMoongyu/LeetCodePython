# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        
        def helper(node):
            nonlocal out
            
            if node is None:
                return
            if node.left is None:
                if node.right is not None:
                    out.append(node.right.val)
            else:
                if node.right is None:
                    out.append(node.left.val)
                    
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return out