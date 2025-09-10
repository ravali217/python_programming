lt=[1,6,6,7,8,8,9]
fre={}
for i in lt:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print(fre)




