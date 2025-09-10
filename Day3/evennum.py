num=list(map(int,input().split()))
countev=0
countod=0
for i in num:
    if i%2==0:
        countev=countev+1
        
    elif i%2!=0:
        countod=countod+1
        
print("even:",countev)
print("odd:",countod)