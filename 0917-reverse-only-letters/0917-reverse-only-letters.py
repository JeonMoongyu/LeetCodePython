class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        len_s = len(s)
        
        def isLetter(c):
            return ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z')
        
        def inRange(i):
            return 0 <= i and i < len_s
        
        left, right = 0, len_s - 1
        
        while True:
            while inRange(left) and not isLetter(s[left]):
                left += 1
            while inRange(right) and not isLetter(s[right]):
                right -= 1
            if not inRange(left) or not inRange(right) or left >= right:
                break
            s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
            left += 1
            right -= 1
        
        return s