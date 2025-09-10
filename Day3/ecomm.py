
def app(lt,el):
    lt.append(el)
    print(lt)
def rem(el):
    lt.remove(el)
    print(lt)
def se(lt,el):
    lt.index(el)
    print(lt)
def dis(lt):
    print(lt)
def total(lt):
    print(len(lt))
def st(lt):
    lt.sort()
    
def clear(lt):
    lt.clear()
    print(lt)
def exit():
    print("exited")
lt=list(input("enter:").split(" "))
el=input("enter:")
app(lt,el)
el=input("enter:")
rem(lt,el)
el=input("enter:")
se(lt,el)
dis(lt)
total(lt)
st(lt)
clear(lt)
exit()




