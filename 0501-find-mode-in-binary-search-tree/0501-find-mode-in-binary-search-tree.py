# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        
        def inorderCount(root):
            if root is None:
                return
            inorderCount(root.left)
            arr.append(root.val)
            inorderCount(root.right)
        
        inorderCount(root)
        
        out = []
        max_cnt = 0
        curr_cnt = 1
        len_arr = len(arr)
        for i in range(1, len_arr + 1):
            if i == len_arr or arr[i-1] != arr[i]:
                if curr_cnt > max_cnt:
                    out = [arr[i-1]]
                    max_cnt = curr_cnt
                elif curr_cnt == max_cnt:
                    out.append(arr[i-1])
                curr_cnt = 1
            else:
                curr_cnt += 1
        return out
        
        