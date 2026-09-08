def toLowerCase(ch):
    # if((ch>='a' and ch<='z') or (ch>=0 or ch<9)):
    #     return ch
    if(ch>='A' or ch<="Z"):
        return chr(ord(ch)-ord('A')+ord('a'))
    else:
        return ch

str="A man, a plan, a canal: Panama"
print(toLowerCase(str[24]))