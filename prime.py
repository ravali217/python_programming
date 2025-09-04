import math
n=int(input())
if n<=1:
    print("not a prime")
else:
    if n>=2:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print("it is not a prime ")
            else:
                print(f"{n} is a prime")
                      
