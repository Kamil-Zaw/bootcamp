menu = ['Espresso', 'Cappuccino', 'Latte', 'Mocha']

stock = {item: 10 for item in menu}

price = {'Espresso': 2.5, 'Cappuccino': 3, 'Latte': 3.5, 'Mocha': 4 }

total_stock_worth = sum(stock[item] * price[item] for item in menu)

 
print("Total Stock Worth:", total_stock_worth)