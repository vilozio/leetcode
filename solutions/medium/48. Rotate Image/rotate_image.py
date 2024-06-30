class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        n = len(matrix) - 1
        # reflect rows
        while i < n:
            matrix[i], matrix[n] = matrix[n], matrix[i]
            i += 1
            n -= 1
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
