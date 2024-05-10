class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        arr = self.countBits(n//2)
        return arr + [ arr[i//2] + i%2 for i in range(n//2+1, n+1) ]