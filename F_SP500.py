# Author: gp1981
# Code generated using ChatGPT 4.0

# Purpose: This module contains functions to retrieve historical and current
# constituents of the S&P500 index and mark them in a given dataframe.

import requests
import pandas as pd

def get_historical_sp500_constituents(API_KEY):
    # Retrieve historical constituents of the S&P500 index
    url = f"https://financialmodelingprep.com/api/v3/historical/sp500_constituent?apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            return df
    print(f"Error retrieving historical S&P500 constituents. Status code: {response.status_code}")
    return None

def get_current_sp500_constituents(API_KEY):
    # Retrieve current constituents of the S&P500 index
    url = f"https://financialmodelingprep.com/api/v3/sp500_constituent?apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            return df
    print(f"Error retrieving current S&P500 constituents. Status code: {response.status_code}")
    return None

def mark_sp500_constituents(df, historical_constituents, current_constituents):
    # Mark S&P500 constituents in the dataframe
    df['is_sp500_constituent'] = False
    if historical_constituents is not None and current_constituents is not None:
        for index, row in df.iterrows():
            date = row['date_x']
            symbol = row['symbol']
            if date in historical_constituents['date'].values:
                if symbol in historical_constituents.loc[historical_constituents['date'] == date]['symbol'].values:
                    df.at[index, 'is_sp500_constituent'] = True
            elif date == current_constituents['date'][0]:
                if symbol in current_constituents['symbol'].values:
                    df.at[index, 'is_sp500_constituent'] = True
    return df