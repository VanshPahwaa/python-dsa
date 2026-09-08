val=input("Enter String")
my_hashtable=[0]*26
for i in val:
    my_hashtable[ord(i)-97]=my_hashtable[ord(i)-97]+1

#  checking frequency
val=input("for which value frequency want to know")
# in this access time is o(1)
print(my_hashtable[ord(val)-ord('a')])