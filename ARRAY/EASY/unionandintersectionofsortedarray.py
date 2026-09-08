def union(arr1,arr2):
    first,second=0,0
    union=[]
    while(first<=len(arr1)-1 and second<=len(arr2)-1):
        if(arr1[first] in union):
            first+=1
        elif(arr2[second] in union):
            second+=1
        else:
            if(arr1[first]<arr2[second]):
                union.append(arr1[first])
                first+=1
            elif(arr1[first]>arr2[second]):
                union.append(arr2[second])
                second+=1
            else:
                union.append(arr1[first])
                first+=1
                second+=1

    while(first<=len(arr1)-1):
        if arr1[first] not in union:
            union.append(arr1[first])
        first+=1
    while(second<=len(arr2)-1):
        if(arr2[second] not in union):
            union.append(arr2[second])
        second+=1
    
    return union

print(union([1,1,1,1,1,1,1],[1,1,1,1,1]))