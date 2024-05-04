# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        if root.left == None and root.right != None:
            return [root.val] + self.inorderTraversal(root.right)
        if root.left != None and root.right == None:
            return self.inorderTraversal(root.left) + [root.val]
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)