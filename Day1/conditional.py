a=10
b=5
#simple if
# if a<b:
#     print("a is big")
# print("Thank you")

# if a>b:
#     print("a is big")
# else:
#     print("b")


# def even(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")

# a=int(input("enter a:"))
# even(a)


# negative or positive
# def num(a):
#     if a>0:
#         print("positive")
#     else:
#         print("negative")
# a=int(input())
# num(a)

# div by  5 and 11
# def num(x):
#     if x%5==0 and x%11==0:
#         print("divisible")
#     else:
#         print("not divisible")

# a=int(input())
# num(a)


# leap year or not 

# def num(x):
#     if (x%4==0 or x%400==0) and x%100!=0:
#         print("leap year")
#     else:
#         print("not a leap  year")


# a=int(input())
# num(a)

# a char is alphabet or not 
# def alp(a):
#     if (a>'a' and a>'z')or (a>'A' and a>'Z'):
#         print("character")
#     else:
#         print("not char")



# a=input("enter:")
# alp(a)



# def num(a):
#     vol="aeiouAEIOU"
#     if x in vol:
#         print("vowel")
#     else:
#         print("NOt a vowel")

# x=input()
# num(x)



#nested if 
def nes(x,y,z):
    if x>y :
        if x>z:
            print("x=",x)
        else:
            print("z=",z)
    else:
        if y>z:
            print("y=",y)
        else:
            print("z=",z)
        
a,b,c=map(int,input().split())
nes(a,b,c)
  
   



