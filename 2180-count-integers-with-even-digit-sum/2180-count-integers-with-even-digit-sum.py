class Solution:
    def countEven(self, num: int) -> int:
        out = 0
        for n in range(1,num+1):
            if self.isValid(n):
                out += 1
        return out
    def isValid(self, n):
        return self.sumDigits(n) % 2 == 0
    def sumDigits(self, n):
        if n < 10:
            return n
        return self.sumDigits(n//10) + n%10