class Solution:
    def alternateDigitSum(self, n: int) -> int:
        arr = list(map(int,str(n)))
        sign = 1
        out = 0
        for digit in arr:
            out += digit * sign
            sign *= -1
        return out