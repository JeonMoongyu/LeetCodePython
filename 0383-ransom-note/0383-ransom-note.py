from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        for c in cnt1.keys():
            if c not in cnt2 or cnt2[c] < cnt1[c]:
                return False
        return True