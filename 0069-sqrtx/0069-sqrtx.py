class Solution:
    def mySqrt(self, x: int) -> int:
        out = 0
        while True:
            if (out+1)**2 > x:
                return out
            out += 1
        