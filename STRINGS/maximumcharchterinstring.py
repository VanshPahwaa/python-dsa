def getmaximumcharachter(str):
    freq=[0]*26
    for i in str:
        freq[ord(i.lower())-97]+=1
    max=0
    for elem in range(0,len(freq)-1):
        if(freq[elem]>freq[max]):
            max=elem

    return chr(max+97)

print(getmaximumcharachter("vanaansh"))
