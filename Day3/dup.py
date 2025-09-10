lt=[1,7,6,5,4,4,5,6,7]
du={}
for i in lt:
    if i in du:
        du[i]+=1
    else:
        du[i]=1
print(du)
print(len(lt)-len(du))