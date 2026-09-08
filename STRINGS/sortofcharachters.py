# class Solution:
#     def findmax(self,my_dict):
#         max_key = max(my_dict, key=my_dict.get)
#         return max_key
        
#     def frequencySort(self, s: str) -> str:
#         freq={}
#         for i in range(0,len(s)):
#             if s[i] not in freq:
#                 freq[s[i]]=0
#             freq[s[i]]+=1
        
#         #generate maximum till len of new is equal to old string
#         newstr=""
#         while(len(newstr)!=len(s)):
#             maxkey=self.findmax(freq)
#             newstr+=maxkey * freq[maxkey]
#             freq[maxkey]=0
#         return newstr
    
#optimised

        



        


        