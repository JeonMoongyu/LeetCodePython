class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0
        space = False
        for c in s:
            if c == " ":
                space = True
            elif space:
                out = 1
                space = False
            else:
                out += 1
        return out
                