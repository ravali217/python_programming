#with args and with return 
def add(x,y):
    c=x+y
    return c
def sub(x,y):
    c=x-y
    return c
def mul(x,y):
    c=x*y
    return c
def div(x,y):
    c=x/y
    return c 
def flo(x,y):
    c=x//y
    return c 
def exp(x,y):
    c=x**y
    return c 
def mod(x,y):
    c=x%y
    return c 

a=int(input("enter a:"))
b=int(input("enter b:"))
z=add(a,b)
z1=sub(a,b)
z2=mul(a,b)
z3=div(a,b) 
z4=mod(a,b)
z5=exp(a,b)
z6=flo(a,b)

print("the add is:",z)
print("the sub is:",z1)
print("the mul is:",z2)
print("the div is:",z3)
print("the mod is:",z4)
print("the exp is:",z5)
print("the flo is:",z6)
print(f"sum is{add(a,b)} ")


