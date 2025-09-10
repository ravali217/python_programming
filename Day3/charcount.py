st=input("enter:")
a=0
d=0
s=0
for i in st:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
print(a)
print(d)
print(s)
