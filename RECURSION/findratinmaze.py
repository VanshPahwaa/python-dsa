def findpath(matrix,path,ans,row,col,isvisited):
    if(row==len(matrix)-1 and col==len(matrix)-1):
        ans.append(path)
        return
    if(check(matrix,row+1,col,isvisited)):
        isvisited[row][col]=True
        path=path+"D"
        findpath(matrix,path,ans,row+1,col,isvisited)
        isvisited[row][col]=False
        path=path[0:len(path)-1]
    if(check(matrix,row,col+1,isvisited)):
        isvisited[row][col]=True
        path=path+"R"
        findpath(matrix,path,ans,row,col+1,isvisited)
        isvisited[row][col]=False
        path=path[0:len(path)-1]
    if(check(matrix,row-1,col,isvisited)):
        isvisited[row][col]=True
        path=path+"U"
        findpath(matrix,path,ans,row-1,col,isvisited)
        isvisited[row][col]=False
        path=path[0:len(path)-1]
    if(check(matrix,row,col-1,isvisited)):
        isvisited[row][col]=True
        path=path+"L"
        findpath(matrix,path,ans,row,col-1,isvisited)
        isvisited[row][col]=False
        path=path[0:len(path)-1]


def check(matrix,row,col,isvisited):
    if(row<0 or row>len(matrix)-1 or col<0 or col>len(matrix)-1):
        return False
    return matrix[row][col]==1 and isvisited[row][col]==False

matrix=[[1,0,0,0],[1,1,0,0],[1,1,0,0],[0,1,1,1]]
ans=[]
isvisited=[[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
findpath(matrix,"",ans,0,0,isvisited)
print(ans)
