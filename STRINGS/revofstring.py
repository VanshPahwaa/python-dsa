def reverse(str):
    i=0
    end=len(str)-1
    # while(i<(end//2)):
    #     temp=str[i]
    #     str[i]=str[end-i]
    #     str[end-i]=temp
    #     i+=1

    while(i<end):
        str[i],str[end]=str[end],str[i]
        i+=1
        end-=1

# str=input("Enter String")
str=['v','a',"n","s","h"]
reverse(str)
print(str)