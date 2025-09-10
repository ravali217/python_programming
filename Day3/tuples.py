t=int(input("enter:"))
deta=[]
for i in range(1,t+1):
    name=input()
    roll=int(input())
    marks=int(input())
    deta.append((name,roll,marks))
print(deta)
max=0
for i in range(len(deta)):
        if deta[i][2]>max:
            max=deta[i][2]
print(max)

for i in range(len(deta)):
        if deta[i][2] >75:
            print(deta[i][2],end=" ")




