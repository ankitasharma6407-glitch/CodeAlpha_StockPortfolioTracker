# Stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 150,
    "MSFT": 300
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:

    # User input
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    # Stop program
    if stock_name == "DONE":
        break

    # Check stock exists
    if stock_name not in stock_prices:
        print("Stock not available.")
        continue

    # Quantity input
    quantity = int(input("Enter quantity: "))

    # Calculate investment
    investment = stock_prices[stock_name] * quantity

    # Add to total
    total_investment += investment

    print(f"{stock_name} Investment Value = ${investment}")

# Final result
print("\n Total Investment Value = $", total_investment)

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("Result saved in portfolio.txt")
