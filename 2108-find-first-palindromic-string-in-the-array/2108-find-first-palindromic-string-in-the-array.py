class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
    def isPalindrome(self, s):
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True