cart={}
n=int(input("enter the range:"))
for i in range(n):
    dname=input("enter name:")
    dprice=float(input("enter the price:"))
    cart[dname]=dprice
   
# price=sum(cart.values())
# print(price)
sum=0
for i in cart.values():
    sum+=i
price=sum
print(sum)
print(price)