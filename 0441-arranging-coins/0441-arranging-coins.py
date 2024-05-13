class Solution:
    def arrangeCoins(self, n: int) -> int:
        out = 0
        while n - (out+1) >= 0:
            out += 1
            n -= out
        return out
        