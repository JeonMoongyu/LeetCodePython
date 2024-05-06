class Solution:
    def longestPalindrome(self, s: str) -> int:
        ourset = set()
        for c in s:
            if c in ourset:
                ourset.remove(c)
            else:
                ourset.add(c)
        return len(s) - max(0, len(ourset)-1)