def insertionsort(my_list):
    for i in range(0,len(my_list)):
        swapped=False
        for j in range(0,len(my_list)-i-1):
            if(my_list[j]>my_list[j+1]):
                my_list[j]=my_list[j]-my_list[j+1]
                my_list[j+1]=my_list[j+1]+my_list[j]
                my_list[j]=my_list[j+1]-my_list[j]
                swapped=True
        if(swapped==False):
            break

my_list=[8,7,6,5,4,3,2,1]
insertionsort(my_list)
print(my_list)