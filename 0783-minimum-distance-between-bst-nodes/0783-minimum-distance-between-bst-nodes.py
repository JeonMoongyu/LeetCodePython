# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = self.InorderTraversal(root)
        out = 10**5
        for i in range(len(arr)-1):
            out = min(arr[i+1]-arr[i], out)
        return out
    def InorderTraversal(self, root):
        if root == None:
            return []
        return self.InorderTraversal(root.left) + [root.val] + self.InorderTraversal(root.right)