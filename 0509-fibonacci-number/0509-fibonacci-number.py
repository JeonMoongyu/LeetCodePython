class Solution:
    def fib(self, n: int) -> int:
        a, b = self.f(n)
        return b
    def f(self, n):
        if n == 0:
            return 0, 0
        if n == 1:
            return 0, 1
        a, b = self.f(n-1)
        return b, a+b