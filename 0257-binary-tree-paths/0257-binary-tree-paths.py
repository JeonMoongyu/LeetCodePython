# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]
        out = []
        if root.left:
            for elem in self.binaryTreePaths(root.left):
                out.append(str(root.val) + "->" + elem)
        if root.right:
            for elem in self.binaryTreePaths(root.right):
                out.append(str(root.val) + "->" + elem)
        return out