import yfinance as yf
import pandas as pd

# Choose the stock ticker
ticker = "AAPL"
ticker2 = "IVR"

# Download historical data
data = yf.download(
    ticker,
    start="2020-01-01",
    end="2024-01-01",
    interval="1d"  # daily data
)

data2 = yf.download(
    ticker2,
    start="2020-01-01",
    end="2024-01-01",
    interval="1d"  # daily data
)

#File path to save the csv files in
file_path = r"C:\Users\furio\Object-Oriented_Python_files\Stock_BackTesting_Engine\CSV_Files\AAPL.csv"
file_path2 = r"C:\Users\furio\Object-Oriented_Python_files\Stock_BackTesting_Engine\CSV_Files\IVR.csv"

# Save to CSV
data.to_csv(file_path)
data2.to_csv(file_path2)

print("Data saved to AAPL_stock_data.csv")
