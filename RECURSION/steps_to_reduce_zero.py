def countsteps(num,c):
    if(num==0):
        return c
    if(num & 1):
        print(f"{num} will be subtracted by 1")
        return countsteps(num-1,c+1)
    else:
        print(f"{num} will be divided by 2")
        return countsteps(num//2,c+1)

print(countsteps(14,0))