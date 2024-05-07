class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        out = 0
        for c in columnTitle:
            out = out * 26 + ord(c) - ord('A') + 1
        return out