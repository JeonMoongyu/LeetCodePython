class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        arr = self.countBits(n-1)
        return arr + [arr[n//2] + n%2]