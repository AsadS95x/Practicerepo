class BudgetApp:
    def __init__(self, description):
        self.description = description
        self.purchaserecord = []
        self.__balance = 0.0

    '''
    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        purchaserecord = ""
        for item in self.purchaserecord:
            # format description and amount
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            # Truncate purchaserecord description and amount to 23 and 7 characters respectively
            purchaserecord += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.__balance)
        return header + purchaserecord + total
        '''

    def deposit(self, amount, description=""):
        self.purchaserecord.append({"amount": amount, "description": description})
        self.__balance += amount

    def withdraw(self, amount, description=""):
        if self.__balance - amount >= 0:
            self.purchaserecord.append({"amount": -1 * amount, "description": description})
            self.__balance -= amount
            return True
        else:
            print("Tried to withdraw ", amount, ". You don't have the necessary funds in your account")
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




food = BudgetApp("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = BudgetApp("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
travel = BudgetApp("Travel")
travel.deposit(1000, "initial deposit")
travel.withdraw(15)

print(food)
print(clothing)
print(travel)


