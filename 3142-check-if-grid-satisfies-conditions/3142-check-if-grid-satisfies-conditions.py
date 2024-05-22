class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for j in range(len(grid[0])):
            if j < len(grid[0])-1 and grid[0][j] == grid[0][j+1]:
                return False
            for i in range(len(grid)-1):
                if grid[i][j] != grid[i+1][j]:
                    return False
        return True