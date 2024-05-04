class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n-m+1):
            satisfied = True
            for j in range(m):
                if haystack[i+j] != needle[j]:
                    satisfied = False
            if satisfied:
                return i
        return -1