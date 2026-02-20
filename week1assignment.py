class DigitalWallet:
    service_name = "PayWay"
    min_balance = 0
    total_wallets = 0
    def __init__(self, owner, balance=0, history=None):
        self.owner = owner
        self.balance = balance
        if history is None:
            self.history = []
        else:
            self.history = history
        DigitalWallet.total_wallets += 1
    def add_funds(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.history.append("+" + str(amount))
            print("Added", amount, ". Balance:", self.balance)
    def spend(self, amount):
        if self.balance - amount >= DigitalWallet.min_balance:
            self.balance = self.balance - amount
            self.history.append("-" + str(amount))
            print("Spent", amount, ". Balance:", self.balance)
        else:
            print("Insufficient balance")
    def display_wallet(self):
        print(f"Owner: {self.owner}, , Balance: {self.balance} , Service: {DigitalWallet.service_name}")

    def show_history(self):
        for item in self.history:
            print(item)
        
wallet = DigitalWallet("Umida", 40)
wallet.display_wallet()
wallet.add_funds(25)
wallet.spend(50)
wallet.spend(10)
wallet.show_history()

print("Total wallets:", DigitalWallet.total_wallets)
# Expected Output

# Owner: Umida, Balance: 40, Service: PayWay
# Added 25. Balance: 65
# Spent 50. Balance: 15
# Spent 10. Balance: 5
# +25
# -50
# -10
# Total wallets: 1