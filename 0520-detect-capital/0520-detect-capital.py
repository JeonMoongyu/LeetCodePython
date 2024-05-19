class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        def isUpper(c):
            return 'A' <= c and c <= 'Z'
        
        def isLower(c):
            return 'a' <= c and c <= 'z'
        
        n = len(word)
        if isUpper(word[0]):
            if n == 1:
                return True
            elif isLower(word[1]):
                for c in word[2:]:
                    if isUpper(c):
                        return False
                return True
            else:
                for c in word[2:]:
                    if isLower(c):
                        return False
                return True
        else:
            for c in word[1:]:
                if isUpper(c):
                    return False
            return True