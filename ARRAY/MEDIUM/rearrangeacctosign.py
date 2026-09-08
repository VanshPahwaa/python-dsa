import sys
sys.max
# class Solution:
#     def rearrangeArray(self, arr: List[int]) -> List[int]:
#         pointer=0
#         while(pointer<=len(arr)-1):
#             if(pointer==0 or pointer%2==0):
#                 if(arr[pointer]<0):
#                     temppointer=pointer
#                     while(arr[temppointer]<0):
#                         temppointer+=1
#                     while(temppointer>pointer):
#                         temp=arr[temppointer]
#                         arr[temppointer]=arr[temppointer-1]
#                         arr[temppointer-1]=temp
#                         temppointer-=1
                
#             elif(pointer%2!=0):
#                 if(arr[pointer]>0):
#                     temppointer=pointer
#                     while(arr[temppointer]>0):
#                         temppointer+=1
#                     while(temppointer>pointer):
#                         temp=arr[temppointer]
#                         arr[temppointer]=arr[temppointer-1]
#                         arr[temppointer-1]=temp
#                         temppointer-=1
                
#             pointer+=1
#         return arr

# optimised
#tc=o(n)
def rearrageacctosign(arr):
    pos,neg=0,1
    newarr=[0]*len(arr)
    i=0
    while(i<=len(arr)-1):
        if(arr[i]>0):
            newarr[pos]=arr[i]
            pos+=2
        else:
            newarr[neg]=arr[i]
            neg+=2
        i+=1
    return newarr

print(rearrageacctosign([3,1,-2,-5,2,-4]))