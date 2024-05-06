class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isPalindrome(s[left+1:right+1]) or self.isPalindrome(s[left:right])
        return True
    def isPalindrome(self, s):
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True