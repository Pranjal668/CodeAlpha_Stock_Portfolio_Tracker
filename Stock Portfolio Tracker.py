import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol} to the portfolio.")

    def remove_stock(self, symbol, quantity):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            if self.portfolio[symbol] > quantity:
                self.portfolio[symbol] -= quantity
                print(f"Removed {quantity} shares of {symbol} from the portfolio.")
            elif self.portfolio[symbol] == quantity:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from the portfolio.")
            else:
                print(f"Error: Not enough shares to remove. You have {self.portfolio[symbol]} shares.")
        else:
            print(f"Error: {symbol} not found in portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return
        print("\nYour current portfolio:")
        for symbol, quantity in self.portfolio.items():
            print(f"{symbol}: {quantity} shares")

    def track_performance(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        total_value = 0
        print("\nCurrent Portfolio Performance:")
        for symbol, quantity in self.portfolio.items():
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")['Close'][-1]  # Get latest closing price
            value = price * quantity
            total_value += value
            print(f"{symbol}: {quantity} shares | Current Price: ${price:.2f} | Total Value: ${value:.2f}")

        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = StockPortfolio()
    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)

        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)

        elif choice == '3':
            portfolio.view_portfolio()

        elif choice == '4':
            portfolio.track_performance()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a valid option (1-5).")

# Run the main function to start the program
main()
