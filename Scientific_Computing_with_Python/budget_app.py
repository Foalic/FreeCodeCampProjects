from collections import OrderedDict

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

        in_dep_descr = "deposit"
        in_dep = self.ledger[0]["amount"]
        formatted_in_dep = "{0:.2f}".format(in_dep)

        initial_deposit = in_dep_descr + (" " * (width_of_descr - len(in_dep_descr))) + (" " * (width_of_amount - len(formatted_in_dep))) + formatted_in_dep

        items = []
        for item in self.ledger:
            amount = item.get("amount")
            if amount >= 0:
                continue
            formatted_amount = "{0:.2f}".format(amount)
            descr = item.get("description")
            if len(descr) > width_of_descr:
                descr = descr[:23]
            items.append(descr + (" " * (width_of_descr -len(descr))) + (" " * (width_of_amount - len(formatted_amount))) + formatted_amount + "\n")

        body = initial_deposit + "\n" + "".join(items)
        return body

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount


    def withdraw(self, amount, description=""):
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


def get_category_namelists_and_amounts_spent(categories):
    name_lists = []
    full_amount_spent = 0

    for category in categories:
        name_lists.append(list(category.name))
        full_amount_spent += category.withdrawn_amount_total

    return name_lists, full_amount_spent


def get_rounded_percentage_of_spent(categories, full_amount_spent):
    percentage_of_full_amount_dict = {}
    rounded_percentages_dict = OrderedDict()

    for category in categories:
        percentage_of_full_amount_dict.update({category.name:((category.withdrawn_amount_total * 100)/full_amount_spent)})
        unrounded_percentage = percentage_of_full_amount_dict.get(category.name)
        rounded_percentage = (unrounded_percentage // 10) * 10
        rounded_percentages_dict.update({category.name:rounded_percentage})

    return rounded_percentages_dict


def get_longest_list_length(name_lists):
    longest_list_length = 0
    for list in name_lists:
        if len(list) > longest_list_length:
            longest_list_length = len(list)
    return longest_list_length


def add_spaces_to_shorter_lists(name_lists):
    longest_list_length = get_longest_list_length(name_lists)
    for list in name_lists:
        if len(list) < longest_list_length:
            for extra_char in range((longest_list_length - len(list))):
                list.append(" ")
    return name_lists


## Function to sort list and format for representation
def make_vertical_category_names(name_lists):
    merged_name_list = add_spaces_to_shorter_lists(name_lists)
    sorted_name_list = []
    first_list = merged_name_list[0]

    for index,char in enumerate(first_list):
        sorted_name_list.append((" " * 5) + f"{first_list[index]} ")

        for second_index, next_list in enumerate(merged_name_list):
            if next_list == first_list:
                continue
            sorted_name_list.append(f" {next_list[index]} ")
            if second_index == (len(merged_name_list) -1) and index == (len(next_list)-1):
                sorted_name_list.append(" ")
                break
            if second_index == len(merged_name_list) -1:
                sorted_name_list.append(" \n")


    vertical_category_names = "".join(sorted_name_list)
    return vertical_category_names


def make_side_bar():
    side_bar_list = []

    for number in range(11):
        number_setup = " " + str(number) + "0|"
        if number == 0:
            number_setup = "  0|"
        elif number == 10:
            number_setup = str(number) + "0|"
        side_bar_list.append(number_setup)
    side_bar_list.reverse()

    return side_bar_list


def make_bars(rounded_percentage_dict):

    side_bar_list = make_side_bar()
    bars_list = []
    for str_number in side_bar_list:
        number = int(str_number[:str_number.find('|')])
        bars = ""
        for category,percentage in rounded_percentage_dict.items():
            if (percentage - number) >= 0:
                bars += " o "
            else:
                bars += " " * 3
        bars_list.append(str_number + bars + " \n")

    bar_chart = "".join(bars_list)
    return bar_chart


def create_spend_chart(categories):
    name_lists, full_amount_spent = get_category_namelists_and_amounts_spent(categories)
    rounded_percentage_dict = get_rounded_percentage_of_spent(categories, full_amount_spent)

    header = "Percentage spent by category\n"
    bars = make_bars(rounded_percentage_dict)
    bar_separator = (" " * 4) + "---" * len(categories) + "-\n"
    vertical_category_names = make_vertical_category_names(name_lists)

    chart = header + bars + bar_separator + vertical_category_names
    return chart
