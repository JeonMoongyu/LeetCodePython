class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        len_s = len(s)
        left, right = 0, len(s)-1
        
        def isVowel(c: chr) -> bool:
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or \
                   c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
        
        while True:
            while left < len_s and not isVowel(s[left]):
                left += 1
            while 0 <= right and not isVowel(s[right]):
                right -= 1
            if left >= right:
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)
        
            