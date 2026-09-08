def print_pattern(row,col):
    if(row==0):
        return 

    if(col<=row):
        print("x",end=" ")
        return print_pattern(row,col+1)
    else:
        print("")
        return print_pattern(row-1,1)
    
print_pattern(4,1)