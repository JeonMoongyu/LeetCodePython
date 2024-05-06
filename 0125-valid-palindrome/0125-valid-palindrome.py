class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.helper(self.convert(s))
    def convert(self, s):
        out = ""
        for c in s:
            if ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z') or ('0' <= c and c <= '9'):
                out = out + c
        return out.lower()
    def helper(self, s):
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True