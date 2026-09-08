# IMPLEMENTING numbering hashing in ARRAY BASED HASHING 
my_arr=[]
size=5
i=0
while(i<size):
    val=int(input(f"Enter value for index {i}"))
    my_arr.append(val)
    i=i+1

# making precomputation for hashing table
ind=0
hashtable=[0]*5
while(ind<len(my_arr)):
    hashtable[my_arr[ind]]=hashtable[my_arr[ind]]+1
    ind+=1

# checking frequency
num=input("for which value frequency want to know")
# in this access time is o(1)
print(hashtable[int(num)])
    