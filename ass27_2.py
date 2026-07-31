class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account holder name :",self.Name)
        print("current balance :",self.Amount)

    def Deposit(self):
        DepositAmount = int(input("Enter amount to deposit : "))
        self.Amount = self.Amount + DepositAmount
        print("Amount deposited successfully.") 

    def Withdraw(self):
        WithdrawAmount = int(input("Enter amount to withdraw : "))

        if WithdrawAmount <= self.Amount:
            self.Amount = self.Amount - WithdrawAmount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():

    obj1 = BankAccount("Prapti", 10000)

    obj1.Display()

    obj1.Deposit()
    obj1.Display()

    obj1.Withdraw()
    obj1.Display()

    print("Interest :", obj1.CalculateInterest())

    print("\n-----------------------------")

    obj2 = BankAccount("Rahul", 5000)

    obj2.Display()

    obj2.Deposit()
    obj2.Display()

    obj2.Withdraw()
    obj2.Display()

    print("Interest :", obj2.CalculateInterest())


if __name__ == "__main__":
    main()