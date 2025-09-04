#checking 
def pro(a):
    if a.isdigit():
        return f"{a }is a digit "
    elif a.isalpha():
        return f"{a } is a character"
    else:
        return f"{a } is a special symbol"
a=input()
print(pro(a))