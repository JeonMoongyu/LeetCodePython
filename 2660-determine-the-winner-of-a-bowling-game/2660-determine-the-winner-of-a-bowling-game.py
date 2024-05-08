class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def f(w):
            if w == 0:
                return 1
            if w == 1 or w == 2:
                return 2
        
        w1, w2 = 0, 0
        score1, score2 = 0, 0
        for a, b in zip(player1, player2):
            score1 += a * f(w1)
            score2 += b * f(w2)
            if a == 10:
                w1 = 2
            elif w1 > 0:
                w1 -= 1
            if b == 10:
                w2 = 2
            elif w2 > 0:
                w2 -= 1
        
        if score1 > score2:
            return 1
        if score1 < score2:
            return 2
        return 0
                