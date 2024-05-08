class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        out = 0
        for l, w in rectangles:
            if min(l, w) > maxLen:
                maxLen = min(l, w)
                out = 1
            elif min(l, w) == maxLen:
                out += 1
        return out