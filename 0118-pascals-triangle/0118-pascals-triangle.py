class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for _ in range(numRows-1):
            arr = out[-1]
            new = [1] + [arr[i-1]+arr[i] for i in range(1,len(arr))] + [1]
            out = out + [new]
        return out
        