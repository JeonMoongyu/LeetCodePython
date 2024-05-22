class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = 2*10**6
        out = []
        for m, n in zip(arr[:-1], arr[1:]):
            if n - m < minDiff:
                out = [[m, n]]
                minDiff = n - m
            elif n - m == minDiff:
                out.append([m, n])
        return out