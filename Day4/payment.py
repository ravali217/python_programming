class payment:
    def pay(self,amount):
        print(f"paid {amount}")
class one(payment):

    def pay(self,amount):
        print(f"paid {amount} card")
class two(payment):
    def pay(self,amount):
        print(f"paid {amount} using credit/debit card")
class three(payment):
    def pay(self,amount):
        print(f"paid {amount} using upi ")
lt=[one(),two(),three()]
for p in lt:
    p.pay(1000)
    
        

