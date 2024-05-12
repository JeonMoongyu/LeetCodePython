from collections import Counter

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        Flush = True
        for i in range(1, 5):
            if suits[0] != suits[i]:
                Flush = False
                break
        if Flush:
            return "Flush"
        M = Counter(ranks)
        for num in M.keys():
            if M[num] >= 3:
                return "Three of a Kind"
        for num in M.keys():
            if M[num] == 2:
                return "Pair"
        return "High Card"