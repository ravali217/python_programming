a=input("enter:")
l={}
for i in a:
    if i in l:
        l[i]+=1
    else:
        l[i]=1

# print(l.keys(),":",l.values())
# print(l.items())
for x in l.items():
    for z in x:
        print(z,end="")
    