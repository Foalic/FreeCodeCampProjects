class Category:
    withdrawn_amount_total = 0

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0


    def __str__(self):
        header = self.make_header_str()
        body = self.make_body_str()
        end_line = "Total: " + "{0:.2f}".format(self.balance)

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
        in_dep = self.ledger[0]["amount"]
        formatted_in_dep = "{0:.2f}".format(in_dep)

        initial_deposit = in_dep_descr + (" " * (width_of_descr - len(in_dep_descr))) + (" " * (width_of_amount - len(formatted_in_dep))) + formatted_in_dep
        for item in self.ledger:
            amount = item.get("amount")
            formatted_amount = "{0:.2f}".format(amount)
            descr = item.get("description")
            items = descr + (" " * (width_of_descr -len(descr))) + (" " * (width_of_amount - len(formatted_amount))) + formatted_amount + "\n"

        body = initial_deposit + "\n" + items
        return body

    def deposit(self, amount, description=""):
        amount = amount
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount


    def withdraw(self, amount, description=""):
        amount = amount
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            self.withdrawn_amount_total += amount
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
    name_lists, full_amount_spent = get_category_namelists_and_amounts_spent(categories)
    rounded_percentage_dict = get_rounded_percentage_of_spent(categories, full_amount_spent)
    header = "Percentage spent by category\n"
    body_list = make_body_list()

    bar_separator = "---" * len(categories) + "-"

    prepped_name_lists = make_vertical_category_names(name_lists)
    chart = prepped_name_lists, full_amount_spent, rounded_percentage_dict, body_list
    return chart


def get_category_namelists_and_amounts_spent(categories):
    name_lists = []
    full_amount_spent = 0

    for category in categories:
        name_lists.append(list(category.name))
        full_amount_spent += category.withdrawn_amount_total

    return name_lists, full_amount_spent


def get_rounded_percentage_of_spent(categories, full_amount_spent):
    percentage_of_full_amount_dict = {}
    rounded_percentages_dict = {}

    for category in categories:
        percentage_of_full_amount_dict.update({category.name:((category.withdrawn_amount_total * 100)/full_amount_spent)})
        unrounded_percentage = percentage_of_full_amount_dict.get(category.name)
        rounded_percentage = (unrounded_percentage // 10) * 10
        rounded_percentages_dict.update({category.name:rounded_percentage})

    return rounded_percentages_dict


def make_body_list():
    body_list = []
    for number in range(11):
        number_setup = " " + str(number) + "0| "
        if number == 0:
            number_setup = "  0| "
        elif number == 10:
            number_setup = str(number) + "0| "
        body_list.append(number_setup)
    body_list.reverse()
    return body_list


def make_vertical_category_names(name_lists):
    longest_list_length = 0
    for list in name_lists:
        if len(list) > longest_list_length:
            longest_list_length = len(list)
    # return longest_list_length

    for list in name_lists:
        if len(list) < longest_list_length:
            for extra_char in range((longest_list_length - len(list))):
                list.append(" ")
    #return name_lists

    ## Need to code a list which combines corresponding indices from each list together



food = Category("food")
clothes = Category("clothes")
food.deposit(200.50, "Aubergine")
food.transfer(100, clothes)

clothes.withdraw(33.24, "petrol")
print(food.ledger)
print(food.balance)

print(clothes.ledger)
print(clothes.get_balance())

print(food)
print(create_spend_chart([food, clothes]))
