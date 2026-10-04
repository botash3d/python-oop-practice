class BankAccount:
    def __init__(self,owner:str="Owner",balance:float=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Amount must be above 0")
        self.balance+=amount
    def withdraw(self,amount):
            if amount>self.balance:
                raise ValueError("Amount cannot be greater than balance")
            self.balance-=amount
    def __str__(self):
        return f"{self.owner} has {self.balance} in bank account."

bank_1=BankAccount("Ashwani")
bank_1.deposit(2000)
bank_1.withdraw(500)
print(bank_1)