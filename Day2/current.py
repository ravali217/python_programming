def num(n):
    for i in range(1,n+1):
        sroll=int(input("enter roll:"))
        sname=input("enter name:")
        cur=int(input("current:"))
        pre=int(input("previous:"))
        total=cur-pre
        print(total)
        bills=total
        if (bills>=1 and bills<=50):
            print(50*3.80)
        elif (bills>50 and bills<=100):
            print((50*3.80)+ ((bills-50)*4.20))
        elif (bills>100 and bills<=200):
            print((50*3.80)+ (50*4.20)+((bills-100)*5.10))
        elif (bills>200 and bills<=300):
            print((50*3.80)+ (50*4.20)+(100*5.10)+((bills-200)*6.30))
        else:
            print((50*3.80)+ (50*4.20)+(100*5.10)+(100*6.30)+((bills-300)*7.50))
n=int(input())
num(n)