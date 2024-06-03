from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        if len(tiles) == 1:
            return 1
        seen = set()
        out = 0
        for i, letter in enumerate(tiles):
            if letter in seen:
                continue
            seen.add(letter)
            out = out + 1 + self.numTilePossibilities(tiles[:i] + tiles[i+1:])
        return out