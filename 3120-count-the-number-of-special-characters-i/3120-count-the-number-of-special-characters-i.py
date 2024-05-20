class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerSeen = set()
        upperSeen = set()
        for c in word:
            if c.isupper() and c not in upperSeen:
                upperSeen.add(c.lower())
            elif c.islower() and c not in lowerSeen:
                lowerSeen.add(c)
        return len(lowerSeen & upperSeen)
                