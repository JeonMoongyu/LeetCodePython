class Solution:
    def maxPower(self, s: str) -> int:
        out, curr = 1, 1
        for c1, c2 in zip(s[:-1], s[1:]):
            if c1 == c2:
                curr += 1
            else:
                out = max(out, curr)
                curr = 1
        out = max(out, curr)
        return out