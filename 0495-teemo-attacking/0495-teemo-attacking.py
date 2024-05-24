class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        out = duration
        for t1, t2 in zip(timeSeries[:-1], timeSeries[1:]):
            if t1 + duration <= t2:
                out += duration
            else:
                out += t2 - t1
        return out