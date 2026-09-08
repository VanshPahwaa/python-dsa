def printspiralmatrix(matrix):
    visited=[[False for i in row] for row in matrix]
    
    row,col=0,0
    i=0
    ans=[]
    while(i<(len(matrix)*len(matrix[0]))):
        #first row
        while col<=len(matrix[row])-1 and visited[row][col]==False:
            ans.append(matrix[row][col])
            i+=1
            visited[row][col]=True
            col+=1

        col-=1
        row+=1
            
        # last column
        while row<=len(matrix)-1 and visited[row][col]==False:
            ans.append(matrix[row][col])
            i+=1
            visited[row][col]=True
            row+=1
            
        row-=1
        col-=1

        # last row
        while col>=0 and visited[row][col]==False:
            ans.append(matrix[row][col])
            i+=1
            visited[row][col]=True
            col-=1
            
        col+=1
        row-=1

        # first column
        while row>=0 and visited[row][col]==False:
            ans.append(matrix[row][col])
            i+=1
            visited[row][col]=True
            row-=1
        row+=1
        col+=1

    return ans
print(printspiralmatrix([[1,2,3],[4,5,6],[7,8,9]]))

