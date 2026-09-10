def selectionsort(my_list):
    for i in range(1,len(my_list)):
        for j in range(i,0,-1):
            # print(j,"hello")
            if(my_list[j]<my_list[j-1]):
                my_list[j]=my_list[j]-my_list[j-1]
                my_list[j-1]=my_list[j-1]+my_list[j]
                my_list[j]=my_list[j-1]-my_list[j]
            

def selectionsort2(my_list):
    for i in range(0,len(my_list)):
        minIndex=i
        for j in range(i+1,len(my_list)):

            if(my_list[j]<my_list[minIndex]):
                minIndex=j
            
        
        my_list[i],my_list[minIndex]=my_list[minIndex],my_list[i]
    print("printing arra",my_list)
            
my_list=[2,4,1,5,7,9,3,6,8]
selectionsort2(my_list)
print(my_list)
