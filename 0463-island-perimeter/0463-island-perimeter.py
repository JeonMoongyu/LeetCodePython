class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def inRange(i, j):
            return 0<=i and i<m and 0<=j and j<n
        
        dis, djs = [-1,0,1,0], [0,1,0,-1]
        out = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    out += 4
                    for di, dj in zip(dis, djs):
                        if inRange(i+di, j+dj) and grid[i+di][j+dj] == 1:
                            out -= 1
        return out