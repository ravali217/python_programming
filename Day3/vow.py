a=input("enter:")
st="aeiouAEIOU"
vc=0
cc=0
for i in a:
    if i in st:
        vc+=1

    else:
        cc+=1
print(vc)
print(cc)
