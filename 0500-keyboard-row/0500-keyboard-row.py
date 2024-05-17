class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = [0,0,0]
        row[0] = "qwertyuiopQWERTYUIOP"
        row[1] = "asdfghjklASDFGHJKL"
        row[2] = "zxcvbnmZXCVBNM"
        M = {}
        for i in range(3):
            for c in row[i]:
                M[c] = i
        out = []
        for word in words:
            satisfied = True
            for c1, c2 in zip(word[:-1], word[1:]):
                if M[c1] != M[c2]:
                    satisfied = False
            if satisfied:
                out.append(word)
        return out