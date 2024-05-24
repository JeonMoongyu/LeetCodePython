# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        left, right = 0, len(arr)-1
        while left < right:
            currSum = arr[left] + arr[right]
            if currSum == k:
                return True
            if currSum > k:
                right -= 1
            elif currSum < k:
                left += 1
        return False
            