class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        outset = set()
        for c in s:
            if c in outset:
                outset.remove(c)
            else:
                outset.add(c)
        return len(outset) <= 1