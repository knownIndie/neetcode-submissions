class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print(matrix)
        # print(matrix[0])
        # print(len(matrix[0]))
        # print(matrix[0][3])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]== target:
                    return True
        else:
            return False