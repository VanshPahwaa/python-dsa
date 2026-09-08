# def rotatematrix(matrix):
#     newmatrix=[[0 for col in elem] for elem in matrix]
#     # empty_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
#     rpointer=0
#     cpointer=len(matrix[0])-1
#     for row in range(0,len(matrix)):
#         rpointer=0
#         for col in range(0,len(matrix[row])):
#             newmatrix[rpointer][cpointer]=matrix[row][col]
#             rpointer+=1
#         cpointer-=1

#     return newmatrix

    # print(newmatrix)

# optimised
def rotatematrix(matrix):
    # first transpose
    # then reverse
    for row in range(0,len(matrix)):
        for col in range(row+1,len(matrix[row])):
            temp=matrix[row][col]
            matrix[row][col]=matrix[col][row]
            matrix[col][row]=temp
    
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[row])//2):
            temp=matrix[row][col]
            matrix[row][col]=matrix[row][len(matrix[row])-1-col]
            matrix[row][len(matrix[row])-1-col]=temp

    return matrix


print(rotatematrix([[1,2,3],[4,5,6],[7,8,9]]))