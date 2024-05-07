class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.rep(s) == self.rep(t)
    def rep(self, s):
        seen = dict()
        n = 1
        out = []
        for c in s:
            if c in seen:
                out += [seen[c]]
            else:
                seen[c] = n
                out += [seen[c]]
                n += 1
        return out