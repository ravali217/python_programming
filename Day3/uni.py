lt=[1,6,6,8,7,9,8,9]
un={}
for i in lt:
    if i in un:
        un[i]+=1
    else:
        un[i]=1
print(un.keys())