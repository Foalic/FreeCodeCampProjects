class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0


    def __str__(self):
        header = self.make_header_str()
        body = self.make_body_str()
        end_line = "Total: " + str(self.balance)

        print_representation = header + body + end_line
        return print_representation


    def make_header_str(self):
        width_of_line = 30
        total_asterisks = width_of_line - len(self.name)

        header = ("*" * (total_asterisks//2)) + self.name + ("*" * (total_asterisks//2))
        if len(header) != width_of_line:
            header += "*" * (width_of_line - len(header))

        return header + "\n"


    def make_body_str(self):
        width_of_descr = 23
        width_of_amount = 7

        in_dep_descr = "initial deposit"
        in_dep = str(self.ledger[0]["amount"])
        initial_deposit = in_dep_descr + (" " * (width_of_descr - len(in_dep_descr))) + (" " * (width_of_amount - len(str(in_dep)))) + in_dep
        for item in self.ledger:
            amount = item.get("amount")
            descr = item.get("description")
            items = descr + (" " * (width_of_descr -len(descr))) + (" " * (width_of_amount - len(str(amount)))) + str(amount) + "\n"

        body = initial_deposit + "\n" + items
        return body

    def deposit(self, amount, description=""):
        amount = float(amount)
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount


    def withdraw(self, amount, description=""):
        amount = float(amount)
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False


    def get_balance(self):
        return self.balance


    def transfer(self, amount, receiving_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {receiving_category.name}")
            receiving_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False


    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True



def create_spend_chart(categories):
    pass


food = Category("food")
clothes = Category("clothes")
food.deposit(200, "Aubergine")
food.transfer(100, clothes)

print(food.ledger)
print(food.balance)

print(clothes.ledger)
print(clothes.get_balance())

print(food)
