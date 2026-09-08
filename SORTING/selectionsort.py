def selectionsort(my_list):
    for i in range(1,len(my_list)):
        for j in range(i,0,-1):
            # print(j,"hello")
            if(my_list[j]<my_list[j-1]):
                my_list[j]=my_list[j]-my_list[j-1]
                my_list[j-1]=my_list[j-1]+my_list[j]
                my_list[j]=my_list[j-1]-my_list[j]
            
my_list=[9,8,7,6,5,4,3,2,1]
selectionsort(my_list)
print(my_list)
