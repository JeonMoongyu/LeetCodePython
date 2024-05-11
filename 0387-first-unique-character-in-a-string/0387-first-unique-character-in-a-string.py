from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        M = Counter(s)
        for i in range(len(s)):
            if s[i] in M and M[s[i]] == 1:
                return i
        return -1