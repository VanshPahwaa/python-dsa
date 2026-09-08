def findsubarray(arr,k):
    maxlen=0
    for i in range(0,len(arr)):
        count=0
        sum=0
        for j in range(i, len(arr)):
            sum+=arr[j]
            if(k==sum):
                count=j-i+1
        maxlen=max(maxlen,count)
    return maxlen


print(findsubarray([1,2,3,4,5],5))