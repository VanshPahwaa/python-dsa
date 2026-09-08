# def compressString(str):
#     ind=0
#     count=1
#     newstr=[]
#     while(ind<=len(str)-1):
#         while(ind<len(str)-1 and str[ind]==str[ind+1]):
#             count+=1
#             ind+=1
        
#         if(count==0):
#             newstr.append(str[ind])    
#         elif(count>=10):
#             newstr.append(str[ind])
#             newstr+=[char for char in str(count)]
#         else:
#             newstr.extend([str[ind],f"{count}"])
#         count=1
#         ind+=1
    
#     return newstr
# str=['a','a','a','b','b','b','b','c','c']
# print(compressString(str))

#Optimized 
class Solution:
    def compress(self, charlist) -> int:
        ind=0
        count=1
        ansIndex=0
        
        while(ind<=len(charlist)-1):
            while(ind<len(charlist)-1 and charlist[ind]==charlist[ind+1]):
                count+=1
                ind+=1
            
            charlist[ansIndex]=charlist[ind]
            ansIndex+=1   
            if(count>1):
                for char in str(count):
                    charlist[ansIndex]=char
                    ansIndex+=1
               
            count=1
            ind+=1
        for i in range(ansIndex,len(charlist)-1):
           del charlist[ansIndex]
        return len(charlist)
    
obj=Solution()
obj.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])