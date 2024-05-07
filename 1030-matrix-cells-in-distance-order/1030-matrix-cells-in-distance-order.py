import numpy as np

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells = dict()
        for i in range(rows):
            for j in range(cols):
                cells[(i,j)] = np.abs(i-rCenter) + np.abs(j-cCenter)
        return sorted(cells.keys(), key = lambda x: cells[x])