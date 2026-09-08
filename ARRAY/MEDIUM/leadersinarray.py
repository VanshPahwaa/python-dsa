import sys
def findleaders(arr):
    max=-sys.maxsize-1
    leaders=[]
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]>max):
            leaders.append(arr[i])
            max=arr[i]
    return leaders


print(findleaders([20,22,12,3,0,6]))
