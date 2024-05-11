class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        len_words = len(words)
        out = 0
        for i in range(len_words):
            for j in range(i+1, len_words):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    out += 1
        return out
    def isPrefixAndSuffix(self, word1, word2):
        len1 = len(word1)
        return word1 == word2[:len1] and word1 == word2[-len1:]
    