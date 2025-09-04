a=int(input())
b=a
c=0
while a>0:
    r=a%10
    c=c+r**3
    a=a//10
if b==c:
    print("is armstrong")
else:
    print("not a armstong")
