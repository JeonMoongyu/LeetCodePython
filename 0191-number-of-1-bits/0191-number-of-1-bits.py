class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n > 0:
            out += n % 2
            n //= 2
        return out