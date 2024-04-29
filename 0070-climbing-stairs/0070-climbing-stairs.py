class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = self.f(n)
        return b
    def f(self, n):
        if n == 1:
            return 0, 1
        if n == 2:
            return 1, 2
        a, b = self.f(n-1)
        return b, a+b