class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        m = len(image)
        n = len(image[0])
        
        def inRange(i,j):
            return 0 <= i and i < m and 0 <= j and j < n
    
        marked = set([(sr,sc)])
        
        def mark(i, j):
            dis, djs = [-1, 0, 1, 0], [0, 1, 0, -1]
            for di, dj in zip(dis, djs):
                if inRange(i+di,j+dj) and image[i+di][j+dj] == image[i][j] and (i+di, j+dj) not in marked:
                    marked.add((i+di, j+dj))
                    mark(i+di, j+dj)
        
        mark(sr,sc)
        for i, j in marked:
            image[i][j] = color
        return image