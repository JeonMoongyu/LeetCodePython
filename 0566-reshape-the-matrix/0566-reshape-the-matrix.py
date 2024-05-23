class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat)*len(mat[0]):
            return mat
        i, j = 0, 0
        out = [[0 for _ in range(c)] for _ in range(r)]
        for row in mat:
            for elem in row:
                out[i][j] = elem
                if j == c-1:
                    i += 1
                    j = 0
                else:
                    j += 1
        return out