class Solution:
    def tribonacci(self, n: int) -> int:
        return self.f(n)[2]
    def f(self, n):
        if n == 0:
            return 0, 0, 0
        if n == 1:
            return 0, 0, 1
        if n == 2:
            return 0, 1, 1
        a, b, c = self.f(n-1)
        return b, c, a+b+c