class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = self.WordToInt(s)
        for _ in range(k):
            n = self.SumDigits(n)
        return n
        
    def WordToInt(self, s):
        out = ""
        for c in s:
            out += self.AlpToIntString(c)
        return int(out)
    
    def AlpToIntString(self, c):
        return str( ord(c) - ord('a') + 1 )
    
    def SumDigits(self, n):
        if n < 10:
            return n
        return self.SumDigits(n//10) + n%10
        