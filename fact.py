def num(n):
        if n==1:
            print(1)
        else:
            fact=1
            for i in range(1,n+1):
                 fact=fact*i
                 print(n-i+1,end="*" if i<n else "=")
n=int(input())
print(num(n))
