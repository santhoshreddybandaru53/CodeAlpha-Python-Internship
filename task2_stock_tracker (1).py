stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 415, "AMZN": 185}

print("Available stocks:", list(stock_prices.keys()))

portfolio = {}

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Try again.")
        continue
    qty = int(input("Enter quantity: "))
    portfolio[stock] = qty

print("\n--- Portfolio Summary ---")
total = 0
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total += value
    print(stock, ":", qty, "shares x $" + str(stock_prices[stock]), "= $" + str(value))

print("Total Investment: $" + str(total))

save = input("Save to file? (yes/no): ")
if save == "yes":
    file = open("portfolio.txt", "w")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        file.write(stock + " - " + str(qty) + " shares - $" + str(value) + "\n")
    file.write("Total: $" + str(total))
    file.close()
    print("Saved to portfolio.txt")
