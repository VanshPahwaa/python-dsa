str='vansh'
count=0
for i in str:
    count+=1
print(count)
i=0
while True:
    try:
        str[i]
        i+=1
    except IndexError:
        break

print(i)