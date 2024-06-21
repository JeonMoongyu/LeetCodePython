class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n
        a = b = 4 * 10**4
        for x, y in ops:
            a = min(a,x)
            b = min(b,y)
        return a*b