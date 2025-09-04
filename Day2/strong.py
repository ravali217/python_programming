n=int(input())
t=n
s=0
while n>0:
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    n=n//10
    s=s+fact
print(s)
    
if t==s:
    print("is strong")
else:
    print("not strong")




