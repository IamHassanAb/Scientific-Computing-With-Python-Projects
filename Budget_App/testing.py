ledger = [{'amount': 1000, 'description': 'initial deposit'}, {'amount': -50, 'description': 'Transfer to Clothing'}, {'amount': 50, 'description': 'Transfer from Food'}, {'amount': -10.15, 'description': 'groceries'}, {'amount': -15.89, 'description': 'restaurant and more food for dessert'}]
stri = "Food"
cat_data = stri.center(30, '#') +"\n"
for i in ledger:
    cat_data += i["description"].ljust(1) + str(i["amount"]).rjust(30- len(i["description"])) + "\n"
print(cat_data)