def isValid( s: str) -> bool:
        n=len(s)
        i=0
        st=[]
        while(i<n):
            if s[i] in ['(','[','{']:
                st.append(s[i])
                i+=1
            else:
                if(len(st)==0):
                    return False
                elif(s[i]== ')'):
                    if st[-1]== '(':
                        i+=1
                        st.pop()
                    else:
                        return False
                elif(s[i]== ']'):
                    if st[-1]== '[':
                        i+=1
                        st.pop()
                    else:
                        return False
                elif(s[i]== '}'):
                    if st[-1]== '{':
                        i+=1
                        st.pop()
                    else:
                        return False
                else:
                    pass
        return len(st)==0

print(isValid("("))