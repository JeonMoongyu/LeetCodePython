class Solution:
    def reverseBits(self, n: int) -> int:
        arr = []
        for _ in range(32):
            arr.append(n%2)
            n //= 2
        out = 0
        for bit in arr:
            out = (out + bit) * 2
        return out // 2