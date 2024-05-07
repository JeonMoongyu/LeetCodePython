class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        M1, M2 = dict(), dict()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for k1, k2 in zip(pattern, s):
            if k1 not in M1 and k2 not in M2:
                M1[k1], M2[k2] = k2, k1
            elif (k1 in M1 and M1[k1] != k2) or (k2 in M2 and M2[k2] != k1):
                return False
        return True
                