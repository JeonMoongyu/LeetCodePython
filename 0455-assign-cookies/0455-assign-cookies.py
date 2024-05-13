class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        out = 0
        i, len_g = 0, len(g)
        for size in s:
            if g[i] <= size:
                out += 1
                i += 1
            if i == len(g):
                break
        return out