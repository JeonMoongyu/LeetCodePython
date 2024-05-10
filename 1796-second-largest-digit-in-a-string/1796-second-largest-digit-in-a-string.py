class Solution:
    def secondHighest(self, s: str) -> int:
        seen = set()
        for c in s:
            if '0' <= c and c <= '9' and int(c) not in seen:
                seen.add(int(c))
        print(seen)
        max_seen, out = -1, -1
        for n in seen:
            if n > max_seen:
                max_seen, out = n, max_seen
            elif n > out:
                out = n
        return out
        