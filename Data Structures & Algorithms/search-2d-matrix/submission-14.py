class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml = len(matrix) * len(matrix[0])
        row ,col = len(matrix),len(matrix[0])
        l,a=0,ml-1
        while l<=a:
            mid = l+(a-l) //2
            r = mid//col
            c = mid%col
            print("mid",mid,"r",r,"c",c,"l",l,"a",a)
            if matrix[r][c]==target:
                return True
            elif matrix[r][c] <target:
                l=mid+1
            else:
                a=mid-1
        return False