def sumofsubsets(superset,ind,sum,ans):
    if(ind==len(superset)):
        ans.append(sum)
        return ans
    sumofsubsets(superset,ind+1,sum+superset[ind],ans)
    return sumofsubsets(superset,ind+1,sum,ans)

ans=[]
print(sumofsubsets([1,2,3,4],0,0,ans))
ans.sort()
print(ans)
