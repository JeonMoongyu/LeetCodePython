class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for m in range(1, n//2 + 1):
            if n % m == 0:
                satisfied = True
                for i in range(m, n):
                    if s[i%m] != s[i]:
                        satisfied = False
                        break
                if satisfied:
                    return True
        return False