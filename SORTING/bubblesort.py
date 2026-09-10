def bubblesort(my_list):
    for i in range(len(my_list)-2,-1,-1):
        for j in range(0,i):
            if(my_list[j]>my_list[j+1]):
                my_list[j]=my_list[j]+my_list[j+1]
                my_list[j+1]=my_list[j]-my_list[j+1]
                my_list[j]=my_list[j]-my_list[j+1]
    print("array after sorting ")
    print(*my_list)

my_list=[2,5,3,8,9,6,4,1]
# my_list=[]
bubblesort(my_list)

