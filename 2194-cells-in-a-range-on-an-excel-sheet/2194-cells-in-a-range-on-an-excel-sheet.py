class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, _, c2, r2 = tuple(s)
        col = [ chr(ord(c1)+i) for i in range(ord(c2)-ord(c1)+1) ]
        row = [ str(j) for j in range(int(r1), int(r2)+1) ]
        out = []
        for c in col:
            for r in row:
                out += [c+r]
        return out