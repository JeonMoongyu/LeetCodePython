class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for c, d in zip(s, t):
            if c != d:
                return d
        return t[-1]