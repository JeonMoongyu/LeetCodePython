class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = [ s[i][::-1] for i in range(len(s)) ]
        return ' '.join(s)