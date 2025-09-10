a=input("enter:")
h={}
for i in a:
    if i in h:
        h[i]+=1
    else:
        h[i]=1
print(max(h,key=h.get))
print(min(h.values()))
