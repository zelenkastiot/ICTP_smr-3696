class Wallet:
    def __init__(self, balance=0):
        self.balance = balance
    
    def add_cash(self, ammount):
        self.balance += ammount

    def spend_cash(self, ammount):
        if ammount > self.balance:
            raise InsufficientAmount
        
        else: 
            self.balance -= ammount

class InsufficientAmount(Exception):
    pass

