class Category:
    name = ""

    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.balance + float(amount)

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance = self.balance - float(amount)
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True

    def check_funds(self, amount):
        return amount <= self.balance

    def __str__(self):
        displayer = ""
        fline = self.name
        fline = fline.center(30, "*").rstrip()
        displayer = displayer + fline + '\n'
        for items in self.ledger:
            item = list(items.values())
            spart = item[0]
            spart = str('%.2f' % spart)
            fpart = item[1]
            fpart = fpart[: 23].ljust(23)
            spart = spart[: 7].rjust(7)
            displayer = displayer + fpart + spart + "\n"
        displayer = displayer + "Total: " + str('%.2f' % self.balance)
        return displayer


length = list()
name = list()
withdrawals = list()
percent = list()


def create_spend_chart(categories):
    for category in categories:
        tmp = 0
        length.append(len(category.name))
        name.append(category.name)
        for items in category.ledger:
            item = list(items.values())
            if item[0] >= 0:
                continue
            else:
                tmp = tmp + (-item[0])
        withdrawals.append(tmp)

    total = sum(withdrawals)
    for x in range(len(withdrawals)):
        per = withdrawals[x] / total
        per = int(round(per, 2) * 100)
        percent.append(per)

    output = "Percentage spent by category\n"
    tmp = 100
    while tmp >= 0:
        output = output.rstrip(" ") + str(tmp).rjust(3) + "| "
        for x in range(len(percent)):
            if tmp <= percent[x]:
                output = output + "o" + "  "
            else:
                output = output + "   "
        tmp = tmp - 10
        output = output + "\n"

    output = output.rstrip(" ") + "    -"
    for x in range(len(percent)):
        output = output.rstrip(" ") + "---"
    output = output + "\n"

    for x in range(max(length)):
        output = output.rstrip(" ") + "     "
        for y in range(len(name)):
            try:
                output = output + name[y][x] + "  "
            except:
                output = output + "   "
        if not x == (max(length) - 1):
            output = output + "\n"

    length.clear()
    name.clear()
    withdrawals.clear()
    percent.clear()
    return output


food_category = Category("Food")
clothing_category = Category("Clothing")
auto_category = Category("Auto")

food_category.deposit(1000, "Initial deposit")
food_category.withdraw(10.15, "Groceries")
food_category.withdraw(15.89, "Restaurant and more foo")
clothing_category.deposit(500, "Initial deposit")
auto_category.deposit(300, "Initial deposit")
auto_category.withdraw(50, "Gas")

print(food_category)
print(clothing_category)
print(auto_category)

print(create_spend_chart([food_category, clothing_category, auto_category]))
