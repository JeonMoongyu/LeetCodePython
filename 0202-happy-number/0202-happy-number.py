class Solution:
    def isHappy(self, n: int) -> bool:
        M = set()
        while n != 1:
            if n in M:
                return False
            M.add(n)
            n = self.sumSquaredDigits(n)
        return True
    def sumSquaredDigits(self, n):
        if n < 10:
            return n**2
        return self.sumSquaredDigits(n//10) + (n%10)**2