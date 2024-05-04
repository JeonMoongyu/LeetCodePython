class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        out = [1]
        for _ in range(rowIndex):
            out = [1] + [out[i-1]+out[i] for i in range(1, len(out))] + [1]
        return out