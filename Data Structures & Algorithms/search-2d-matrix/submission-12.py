class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c= len(matrix[0])-1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][c]:
                a=0
                b=len(matrix[0])-1
                while a<=b:
                    m=(a+b)//2

                    if matrix[i][m]== target:
                        return True
                    elif matrix[i][m]<target:
                        a=m+1
                    else:
                        b=m-1
            
        else:
            return False
