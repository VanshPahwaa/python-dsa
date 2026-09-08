class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowset=set()
        colset=set()
        for row in range(0,len(matrix)):
            for col in range(0,len(matrix[row])):
                if(matrix[row][col]==0):
                    rowset.add(row)
                    colset.add(col)
        # making whole row zero
        for row in rowset:
            for col in range(0,len(matrix[row])):
                matrix[row][col]=0
        
        for col in colset:
            for row in range(0,len(matrix)):
                matrix[row][col]=0

        return matrix

        