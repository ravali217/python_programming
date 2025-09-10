n=int(input())
s=0
l=0
f=0
while n>0:
    r=n%10
    if l==0:
        l=r
    f=r
    n=n//10
print(l+f)