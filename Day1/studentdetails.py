#program to enter student number,student name,3 subjects of marks,cal total and average of students ,print all students details
n=int(input())
for i in range(1,n+1):
    sroll=int(input("enter roll:"))
    sname=input("enter name:")
    phy,mat,che=map(int,input().split())
    total=phy+mat+che
    print(f"{total:.2f} marks")
    avg=total/3
    print(f"{avg:.2f} average marks")   
    print(sroll,sname,total,avg)
