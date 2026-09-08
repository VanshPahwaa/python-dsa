# optimised
def setmatrixzero(nums):
    rowcol0=1
    for row in range(0,len(nums)):
        for col in range(0,len(nums[row])):
            if(nums[row][col]==0):
                if(col==0):
                    rowcol0=0
                else:
                    # marking row zero
                    nums[0][col]=0

                # marking col zero
                nums[row][0]=0

    
    print(rowcol0)

    for row in range(len(nums)-1,-1,-1):
        for col in range(len(nums[row])-1,-1,-1):
            if(col==0):
                if(nums[row][0]==0 or rowcol0==0):
                    nums[row][col]=0
            else:
                if(nums[0][col]==0 or nums[row][0]==0):
                    nums[row][col]=0
                
    return 

# optimised
# def setmatrixzero(nums):
#     col0 = 1
#     # step 1: Traverse the matrix and
#     # mark 1st row & col accordingly:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 # mark i-th row:
#                 matrix[i][0] = 0

#                 # mark j-th column:
#                 if j != 0:
#                     matrix[0][j] = 0
#                 else:
#                     col0 = 0

#     # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
#     for i in range(1, n):
#         for j in range(1, m):
#             if matrix[i][j] != 0:
#                 # check for col & row:
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0

#     #step 3: Finally mark the 1st col & then 1st row:
#     if matrix[0][0] == 0:
#         for j in range(m):
#             matrix[0][j] = 0
#     if col0 == 0:
#         for i in range(n):
#             matrix[i][0] = 0

#     return matrix
# striver questions


# nums=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
nums=[[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
# nums=[[1],[0]]
setmatrixzero(nums)
for i in nums:
    print(i)


            

