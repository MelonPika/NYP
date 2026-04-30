# John bought 2000 shares at $0.40 each
shares = 2000
buy_price = 0.40
buy_commission_rate = 0.03
sell_commission_rate = 0.02

# Input current selling price
sell_price = float(input("Enter current price for ABC Bank Corporation (S$):"))

# Buying calculations
buy_amount = shares * buy_price
buy_commission = buy_amount * buy_commission_rate

# Selling calculations
sell_amount = shares * sell_price
sell_commission = sell_amount * sell_commission_rate

# Total commission
total_commission = buy_commission + sell_commission

# Profit or loss
profit_loss = sell_amount - buy_amount - total_commission

# Output
print("You paid total commission of (S$)", total_commission)

if profit_loss > 0:
    print("You have made a profit of (S$)", profit_loss)
elif profit_loss < 0:
    print("You have made a loss of (S$)", abs(profit_loss))
else:
    print("You have broken even")