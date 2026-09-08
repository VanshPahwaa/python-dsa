# optimised
def printspiralmatrix(nums):
    top,left=0,0
    right=len(nums[0])-1
    bottom=len(nums)-1
    ans=[]
    while(left<=right and top <=bottom):
        for i in range(left,right+1):
            ans.append(nums[top][i])
        top+=1

        for i in range(top,bottom+1):
            ans.append(nums[i][right])

        right-=1
        if(top<=bottom):
            for i in range(right,left-1,-1):
                ans.append(nums[bottom][i])
            bottom-=1
        if(left<=right):
            for i in range(bottom,top-1,-1):
                ans.append(nums[i][left])

            left+=1
    return ans

print(printspiralmatrix())

    
 



                
