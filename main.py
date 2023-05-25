# Author: gp1981
# Project start date: 17 Mar 2023
# Code generated using ChatGPT 4.0

# Purpose: This code analyzes financial data by downloading and processing the data
# from financialmodelingprep.com API.

import os
from dotenv import load_dotenv
from tqdm import tqdm
from F_API import *
from F_SP500 import *

# Load API key from .env file in the root directory
load_dotenv()
API_KEY = os.environ.get('API_KEY')

# Download list of stocks
stock_list = download_stock_list(API_KEY)

# Download financial statements for the first 10 stocks
num_stocks_to_download = 20
limit_download = 12
stocks_to_download = stock_list['symbol'].iloc[:num_stocks_to_download]

dfs = []
for ticker in tqdm(stocks_to_download, desc="Downloading financial data", unit="stock", leave=False):
    balance_sheet = download_balance_sheet(API_KEY, stock_list[stock_list['symbol'] == ticker], limit_download)
    income_statement = download_income_statement(API_KEY, stock_list[stock_list['symbol'] == ticker], limit_download)
    cash_flow = download_cash_flow(API_KEY, stock_list[stock_list['symbol'] == ticker], limit_download)
    key_metrics = download_key_metrics(API_KEY, ticker)
    profile = download_profile(API_KEY, ticker)

    if balance_sheet.empty or income_statement.empty or cash_flow.empty or key_metrics.empty or profile.empty:
        print(f"Financial data is missing for stock {ticker}")
    else:
        df = combine_dataframes(stock_list[stock_list['symbol'] == ticker], balance_sheet, income_statement, cash_flow, key_metrics, profile)
        dfs.append(df)

# Concatenate dataframes for all downloaded stocks into one dataframe
df = pd.concat(dfs, ignore_index=True)

# Retrieve historical and current S&P500 constituents
historical_constituents = get_historical_sp500_constituents(API_KEY)
current_constituents = get_current_sp500_constituents(API_KEY)

# Mark S&P500 constituents in the dataframe
df = mark_sp500_constituents(df, historical_constituents, current_constituents)

print(df.head())