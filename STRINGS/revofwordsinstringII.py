class Solution:
    def reverseWords(self, str: str) -> str:
        ind=0
        prevspace=True
        reversed=""
        start=0
        while(ind<=len(str)-1):
            if(str[ind]==" "):
                
                if(prevspace==False):
                    if(start-1<0):
                        reversed+=str[ind-1::-1]
                    else:
                        reversed+=str[ind-1:start-1:-1]
                prevspace=True
                reversed+=(" ")
            elif(str[ind]!=" " and prevspace==True):
                start=ind
                prevspace=False
            else:
                pass
            ind+=1

        if(prevspace==False):
            if(start-1<0):
                        reversed+=str[ind-1::-1]
            else:
                        reversed+=str[ind-1:start-1:-1]
        return reversed
    


obj=Solution()
print(obj.reverseWords("Let's take LeetCode contest"))

# char* reverseWords(char* s) {
#     int n = strlen(s);
#     int start = 0, end = 0;

#     while (end <= n) {
#         if (s[end] == ' ' || s[end] == '\0') {
#             int left = start, right = end - 1;
#             while (left < right) {
#                 char temp = s[left];
#                 s[left] = s[right];
#                 s[right] = temp;
#                 left++;
#                 right--;
#             }
#             start = end + 1;
#         }
#         end++;
#     }

#     return s;
# }