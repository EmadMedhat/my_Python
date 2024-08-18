import datetime


class bank_acc():
    def __init__(self,name,amount):
        self.name=name
        self.balance=amount
        self.date=datetime.datetime.now().replace(microsecond=0)
        print(f"\nthis account has been created successfully \n name:{self.name}\n balance=${self.balance:.2f}\n date of initlizaition: {self.date}")
   
    def get_balance(self):
        print(f" name:{self.name}\n balance=${self.balance:.2f}")
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"in {self.date} a deposit of ${amount}  completed..")
        self.get_balance()
        
    def ViableTransaction(self,amount):
        if self.balance >=amount:
            return
        else:
            raise Exception(f"\n account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self,amount):
        try:
            self.ViableTransaction(amount)
        except Exception as error :
            print(f"withdraw failed.. {error}")
        else:
            self.balance=self.balance-amount
            print(f"in {self.date} a withdraw of ${amount} completed..")
            self.get_balance()
    
    def transfer(self,tras_name,trans_amount):
        try:
            self.ViableTransaction(trans_amount)
        except Exception as error :
            print(f"transfer failed.. {error}")
        else:
            self.withdraw(trans_amount)
            tras_name.deposit(trans_amount)
            print(f"in {self.date}, transfer from {self.name} to {tras_name.name} has done")

    
