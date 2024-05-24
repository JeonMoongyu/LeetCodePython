# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = {root:0}
        sums = {}
        cnts = {}
        Q = deque([root])
        
        while Q:
            node = Q.popleft()
            l = levels[node]
            if node.left is not None:
                levels[node.left] = l + 1
                Q.append(node.left)
            if node.right is not None:
                levels[node.right] = l + 1
                Q.append(node.right)
            if l in sums:
                sums[l] += node.val
                cnts[l] += 1
            else:
                sums[l] = node.val
                cnts[l] = 1
        
        out = []
        for l in sorted(list(sums.keys())):
            out.append(sums[l]/cnts[l])
        return out