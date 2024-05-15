class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        len0, len1, cur0, cur1 = 0, 0, 0, 0
        for c in s:
            if c == '0':
                len1 = max(len1, cur1)
                cur1 = 0
                cur0 += 1
            else:
                len0 = max(len0, cur0)
                cur0 = 0
                cur1 += 1
        len0 = max(len0, cur0)
        len1 = max(len1, cur1)    
        return len0 < len1