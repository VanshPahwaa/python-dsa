def findpalindromepartition(str,partition,ans,ind):
    if(ind>=len(str)):
        ans.append(partition.copy())
        return
    for i in range(ind,len(str)):
        if(ispali(str[ind:i+1])):
            partition.append(str[ind:i+1])
            findpalindromepartition(str,partition,ans,i+1)
            partition.pop()

def ispali(str):
    # print(str,"".join(reversed(str)))
    return (str=="".join(reversed(str)))

# print(ispali("a"))
ans=[]
findpalindromepartition("aabb",[],ans,0)
print(ans)