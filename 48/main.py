from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        i, j = 0, n-1
        while i < j:
            for k in range(n):
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
            i += 1
            j -= 1
        return
if __name__ == "__main__":
    s = Solution()
    matrix = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
    ]
    s.rotate(matrix)
    print(matrix)