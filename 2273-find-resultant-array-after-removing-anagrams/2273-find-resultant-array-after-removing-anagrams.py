class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 0
        while i < len(words)-1:
            if sorted(words[i]) == sorted(words[i+1]):
                words = words[:i+1] + words[i+2:]
            else:
                i += 1
        return words