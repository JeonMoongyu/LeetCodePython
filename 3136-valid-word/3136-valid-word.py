class Solution:
    def isValid(self, word: str) -> bool:
        
        def isValidChar(c):
            return '0'<=c and c<='9' or 'a'<=c and c<='z' or 'A'<=c and c<='Z'
        
        def isVowel(c):
            return c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or \
                   c=='A' or c=='E' or c=='I' or c=='O' or c=='U'
        
        def isConsonant(c):
            return ('a'<=c and c<='z' or 'A'<=c and c<='Z') and not isVowel(c)
        
        if len(word) < 3:
            return False
        
        cnt_vowel, cnt_consonant = 0, 0
        for c in word:
            if not isValidChar(c):
                return False
            if isVowel(c):
                cnt_vowel += 1
            elif isConsonant(c):
                cnt_consonant += 1
        
        return cnt_vowel >= 1 and cnt_consonant >= 1