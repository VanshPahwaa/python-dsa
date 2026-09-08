str="my name is vansh"

def revofwords(str):
    
    end=len(str)-1
    right=end
    prevspace=True
    reverse=""
    while(end>=0):
        if(str[end]!=" " and prevspace==True):
            right=end
            prevspace=False
        if(str[end]==" " and prevspace==False):
            reverse=reverse+str[end+1:right+1]+" "
            prevspace=True
        end-=1
    
    if(prevspace==False):
        reverse=reverse+str[end+1:right+1]
    if(prevspace==True):
        reverse=reverse[0:len(str)-2]
    return reverse

print(f"'{revofwords(str)}'")

