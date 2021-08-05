class Category:

    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.bal = 0

    def __repr__(self):

        # Source: https://forum.freecodecamp.org/t/python-budget-app-hints-and-tips/423060(Point No#4)

        title = f'''{self.category.center(30, '*')}\n'''
        items = ''
        total = 0
        for item in self.ledger:

            items += f'''{item["description"][0:23]:23}''' + f'''{item["amount"]:>7.2f}''' +"\n"
            total += item['amount']
        output = title + items + 'Total: ' + str(total)
        return output

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount,
                           'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount,
                               'description': description})
            return True
        else:
            return False

    def transfer(self, amount, c):
        if self.check_funds(amount):
            self.withdraw(amount, f'''Transfer to {c.category}''')
            c.deposit(amount,f'''Transfer from {self.category}''')

            return True
        else:

            return False

    def check_funds(self, amount):
        if amount > self.get_balance():

            return False

        return True

    def get_balance(self):
        bal = self.bal
        for i in self.ledger:
            bal = bal + i['amount']

        return bal

    def get_withdrawls(self):
        Withdrawls = 0
        for items in self.ledger:
            if items['amount'] < 0:
                Withdrawls += abs(items['amount'])

        return Withdrawls


def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    percentageList = [
        '100',
        '90',
        '80',
        '70',
        '60',
        '50',
        '40',
        '30',
        '20',
        '10',
        '0',
        ]
    totalSpent = 0
    for items in categories:
        totalSpent += round(items.get_withdrawls(), 2)
    nameList = [items.category for items in categories]
    eachSpentList = [items.get_withdrawls() for items in categories]
    percentSpentList = [round(items / totalSpent, 2) * 100 for items in
                        eachSpentList]

    for element in percentageList:
        chart += element.rjust(3) + '| '
        for percent in percentSpentList:
            if int(element) <= percent:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'

    chart += '    ----' + '---' * (len(nameList) - 1)
    chart += '\n     '

    length = 0
    for names in nameList:
        if length < len(names):
            length = len(names)

    for i in range(length):
        for name in nameList:
            if len(name) > i:
                chart += name[i] + '  '
            else:
                chart += '   '
        if i < length - 1:
            chart += '\n     '

    return chart