a=int(input())
d=int(input())
try:
    print(a/d)
except  Exception  as e :
    print("division error")
    print(e)
else:
    print("successfully done")
finally:
    print("done")
