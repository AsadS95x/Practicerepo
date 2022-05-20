from unicodedata import category


class BudgetApp:
    def __init__(self, description):
        self.description = description
        self.purchaserecord = []
        self.__balance = 0.0

    
    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        purchaserecord = ""
        for item in self.purchaserecord:
            # format description and amount
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            # Truncate purchaserecord description and amount to 23 and 7 characters respectively
            purchaserecord += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.__balance).center(30)

        print("\n Written to ", self.description, ".txt")
        fn =self.description+".txt"
        # print(fn)
        file = open(fn, "w")
        file.write("Did this work???\n")
        file.write(header + purchaserecord + total)
        file.close

        return header + purchaserecord + total
        

    def deposit(self, amount, description=""):
        self.purchaserecord.append({"amount": amount, "description": description})
        self.__balance += amount

    def withdraw(self, amount, description=""):
        if self.__balance - amount >= 0:
            self.purchaserecord.append({"amount": -1 * amount, "description": description})
            self.__balance -= amount
            return True
        else:
            self.purchaserecord.append({"amount": amount, "description": "Withdraw Cancelled"})
            self.purchaserecord.append({"amount": 0, "description": "Not enough funds"})
            return False

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, transferlocation):
        if self.withdraw(amount, "Transfer to {}".format(transferlocation.description)):
            transferlocation.deposit(amount, "Transfer from {}".format(self.description))
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.__balance >= amount:
            return True
        else:
            return False


