n=int(input())
for i in range(1,n+1):
    if str(i)==str(i)[::-1]:
        
        print("is palindrome")
    else:
        print("not palindrome")