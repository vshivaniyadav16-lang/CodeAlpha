# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_value = 0

print("Available Stocks:")
for stock, price in stocks.items():
    print(stock, ":", price)

n = int(input("\nHow many stocks do you want to enter? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stocks:
        investment = stocks[stock_name] * quantity
        total_value += investment
        print("Investment in", stock_name, "=", investment)
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_value)

# Optional: Save result in a text file
file = open("portfolio_result.txt", "w")
file.write("Total Investment Value = " + str(total_value))
file.close()

print("Result saved in portfolio_result.txt")


