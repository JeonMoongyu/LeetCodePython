class Solution:
    def removeVowels(self, s: str) -> str:
        s = list(s)
        
        def isVowel(c: chr) -> bool:
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'
        
        for i in range(len(s)):
            if isVowel(s[i]):
                s[i] = ''
        
        return ''.join(s)
        