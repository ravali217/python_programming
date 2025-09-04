def fun(n):
    for i in range(1,n+1):
        sroll=int(input("enter the roll:"))
        sname=input("enter name:")
        phy,che,mat=map(int,input().split())
        total=(phy+che+mat)
        print(total)
        aver=(phy+che+mat)/3
        print(aver)
        if phy>40 and che>40 and mat>40:
            if (aver<50):
                print("c grade")
            elif (aver<70 and aver>=50):
                print("b grade")
            elif (aver>=70 and aver<80):
                print("A grade")
            else:
                print("distention")
        else:
            print("below 40 is fail")
n=int(input("enter students in no:"))
fun(n)

