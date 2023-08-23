class BankAccount:
    def __init__(self,account_number,balance,costumerId):
        self.x=account_number
        self.y=balance
        self.z=costumerId
    def deposit(self,amount):
        self.y+=amount
    def withdraw(self,amount):
        self.y-=amount
    def get_balance(self):
        return self.y
    def __str__(self):
        return "#account: "+str(self.x)+"\n balance: "+str(self.y)+"\n costumerId: "+str(self.z)

a1=BankAccount("123456789",7000,"moosavi")
a1.deposit(100)
print(a1.get_balance())
a1.withdraw(500)
print(a1.get_balance())
print(a1)