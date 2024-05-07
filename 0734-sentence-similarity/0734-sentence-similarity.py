class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        for word1, word2 in zip(sentence1, sentence2):
            if not self.areWordsSimilar(word1, word2, similarPairs):
                return False
        return True
    def areWordsSimilar(self, word1, word2, similarPairs):
        return word1 == word2 or [word1, word2] in similarPairs or [word2, word1] in similarPairs