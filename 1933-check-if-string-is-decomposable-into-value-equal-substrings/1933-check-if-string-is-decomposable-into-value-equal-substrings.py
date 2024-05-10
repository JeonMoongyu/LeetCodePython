class Solution:
    def isDecomposable(self, s: str) -> bool:
        used = False
        len_s = len(s)
        i = 0
        while i < len_s:
            if i + 2 < len_s and s[i] == s[i+1] and s[i+1] == s[i+2]:
                i += 3
            elif not used and i + 1 < len_s and s[i] == s[i+1]:
                i += 2
                used = True
            else:
                return False
        return used
        