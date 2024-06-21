class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = len(words)
        out = []
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                if self.isSubstring(words[i], words[j]) and words[i] not in out:
                    out.append(words[i])
        return out
        
    def isSubstring(self, word1: str, word2: str) -> bool:
        len1, len2 = len(word1), len(word2)
        if len1 > len2:
            return False
        for i in range(len2 - len1 + 1):
            if word1 == word2[i:i+len1]:
                return True
        return False
            
        