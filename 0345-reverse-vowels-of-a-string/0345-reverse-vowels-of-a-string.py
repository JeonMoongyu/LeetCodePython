class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        while True:
            while left < len(s) and s[left] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                left += 1
            while right >= 0 and s[right] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                right -= 1
            if left >= right:
                break
            s = s[:left] + s[right] + s[left+1:right] + s[left] + s[right+1:]
            left += 1
            right -= 1
        return s
            