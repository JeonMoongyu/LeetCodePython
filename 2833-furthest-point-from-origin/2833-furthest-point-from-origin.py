class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt1, cnt2 = 0, 0
        for move in moves:
            if move == 'L':
                cnt1 -= 1
            elif move == 'R':
                cnt1 += 1
            else:
                cnt2 += 1
        return abs(cnt1) + cnt2