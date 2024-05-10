import sys
sys.setrecursionlimit(10**7)

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0