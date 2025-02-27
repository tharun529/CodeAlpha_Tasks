import yfinance as yf
import pandas as pd

# Portfolio dictionary to store stocks and quantities
portfolio = {}

# Function to add stock
def add_stock(symbol, quantity):
    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity
    print(f"✅ Added {quantity} shares of {symbol}")

# Function to remove stock
def remove_stock(symbol, quantity):
    if symbol in portfolio:
        if portfolio[symbol] > quantity:
            portfolio[symbol] -= quantity
            print(f"❌ Removed {quantity} shares of {symbol}")
        else:
            del portfolio[symbol]
            print(f"❌ Removed {symbol} from portfolio")
    else:
        print("⚠ Stock not found!")

# Function to get stock prices and portfolio value
def get_portfolio_value():
    total_value = 0
    data = []
    
    for symbol, quantity in portfolio.items():
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"].iloc[-1]  # Get latest closing price
        value = price * quantity
        total_value += value
        data.append([symbol, quantity, price, value])
    
    df = pd.DataFrame(data, columns=["Stock", "Quantity", "Price", "Total Value"])
    print("\n📊 Portfolio Summary:")
    print(df)
    print(f"\n💰 Total Portfolio Value: ${total_value:.2f}")

# Example Usage
add_stock("AAPL", 5)  # Add Apple stock
add_stock("GOOGL", 2) # Add Google stock
get_portfolio_value()   # Show portfolio value
remove_stock("AAPL", 2) # Remove 2 Apple stocks
get_portfolio_value()   # Show updated portfolio
