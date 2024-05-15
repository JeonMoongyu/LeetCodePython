class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        out = 0
        while z > 0:
            out += z % 2
            z //= 2
        return out