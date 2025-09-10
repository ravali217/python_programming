a=input("enter:")
occ={}
for i in a:
    if i in occ:
        occ[i]+=1
    else:
        occ[i]=1
print(occ)