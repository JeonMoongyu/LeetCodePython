class Solution:
    def toLowerCase(self, s: str) -> str:
        out = ""
        for c in s:
            if 'A' <= c and c <= 'Z':
                out += chr(ord(c) - ord('A') + ord('a'))
            else:
                out += c
        return out 