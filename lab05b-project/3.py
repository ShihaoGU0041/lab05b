class BankAccount:
    def __init__(self, name, balance=0, currency="EUR"):
        self.name     = name
        self.balance  = balance
        self.currency = currency

    def deposit(self, amount, description="Deposit"):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        print(f"{description}: +{amount:.2f} {self.currency}")

    def withdraw(self, amount, description="Withdrawal"):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"{description}: -{amount:.2f} {self.currency}")


acc = BankAccount("Alice", 1000)
acc.deposit(500)                     # 用默认描述 "Deposit"
acc.deposit(200, "Salary")           # 自定义描述
acc.withdraw(100, description="Rent")

