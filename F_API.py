# Author: gp1981
# Purpose: Library for downloading financial data from financialmodelingprep.com API
#          including balance sheets, income statements, cash flows, key metrics, and company profiles
# Project start date: 05 May 2023
# Notes:

import pandas as pd
import requests
from tqdm import tqdm

def download_stock_list(API_KEY):
    """
    Download the list of stocks from financialmodelingprep.com API.

    Parameters:
        API_KEY (str): API key for financialmodelingprep.com API.

    Returns:
        pandas.DataFrame: DataFrame containing the list of stocks.
    """
    url = f'https://financialmodelingprep.com/api/v3/stock/list?apikey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            stock_list = pd.DataFrame(data, index=range(len(data)))
            return stock_list
        else:
            print('Empty response from API')
            return None
    else:
        print(f'Response status code: {response.status_code}')
        return None

def download_financials(API_KEY, stock_list, statement, limit_download):
    """
    Download financial statements for the given stock list and statement type from financialmodelingprep.com API.

    Parameters:
        API_KEY (str): API key for financialmodelingprep.com API.
        stock_list (pandas.DataFrame): DataFrame containing the list of stocks.
        statement (str): Statement type ('balance-sheet-statement', 'income-statement', 'cash-flow-statement').
        limit_download (int): Number of periods to download.

    Returns:
        pandas.DataFrame: Combined DataFrame of the downloaded financial statements.
    """
    dfs = []
    for symbol in tqdm(stock_list['symbol']):
        url = f"https://financialmodelingprep.com/api/v3/{statement}/{symbol}?period=quarter&limit={limit_download}&apikey={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                df = pd.json_normalize(data)
                df['symbol'] = symbol
                dfs.append(df)
    if len(dfs) > 0:
        return pd.concat(dfs, ignore_index=True)
    else:
        return None

def download_balance_sheet(API_KEY, stock_list, limit_download):
    """
    Download the balance sheet for the given stock list from financialmodelingprep.com API.

    Parameters:
        API_KEY (str): API key for financialmodelingprep.com API.
        stock_list (pandas.DataFrame): DataFrame containing the list of stocks.
        limit_download (int): Number of periods to download.

    Returns:
        pandas.DataFrame: DataFrame containing the balance sheet data.
    """
    return download_financials(API_KEY, stock_list, 'balance-sheet-statement', limit_download)

def download_income_statement(API_KEY, stock_list, limit_download):
    """
    Download the income statement for the given stock list from financialmodelingprep.com API.

    Parameters:
        API_KEY (str): API key for financialmodelingprep.com API.
        stock_list (pandas.DataFrame): DataFrame containing the list of stocks.
        limit_download (int): Number of periods to download.

    Returns:
        pandas.DataFrame: DataFrame containing the income statement data.
    """
    return download_financials(API_KEY, stock_list, 'income-statement', limit_download)

def download_cash_flow(API_KEY, stock_list, limit_download):
    """
    Download the cash flow statement for the given stock list from financialmodelingprep.com API.

    Parameters:
        API_KEY (str): API key for financialmodelingprep.com API.
        stock_list (pandas.DataFrame): DataFrame containing the list of stocks.
        limit_download (int): Number of periods to download.

    Returns:
        pandas.DataFrame: DataFrame containing the cash flow statement data.
    """
    return download_financials(API_KEY, stock_list, 'cash-flow-statement', limit_download)

def download_key_metrics(API_KEY, stock_list):
    """
    Download the key metrics for the given stock list from financialmodelingprep.com API.

    Parameters:
        API_KEY (str): API key for financialmodelingprep.com API.
        stock_list (pandas.DataFrame): DataFrame containing the list of stocks.

    Returns:
        pandas.DataFrame: DataFrame containing the key metrics data.
    """
    url = f"https://financialmodelingprep.com/api/v3/company-key-metrics/{stock_list}?apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    key_metrics = pd.DataFrame(data)
    return key_metrics

def download_profile(API_KEY, stock_list):
    """
    Download the company profile for the given stock list from financialmodelingprep.com API.

    Parameters:
        API_KEY (str): API key for financialmodelingprep.com API.
        stock_list (pandas.DataFrame): DataFrame containing the list of stocks.

    Returns:
        pandas.DataFrame: DataFrame containing the company profile data.
    """
    url = f"https://financialmodelingprep.com/api/v3/company/profile/{stock_list}?apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    profile = pd.DataFrame.from_dict(data)
    return profile

def combine_dataframes(stock_list, *dfs):
    """
    Combine the stock list DataFrame with other DataFrames.

    Parameters:
        stock_list (pandas.DataFrame): DataFrame containing the list of stocks.
        *dfs: Variable length list of DataFrames to be combined.

    Returns:
        pandas.DataFrame: Combined DataFrame.
    """
    df_merged = stock_list
    for df in dfs:
        if df is not None:
            df_merged = pd.merge(df_merged, df, on='symbol', how='outer')
    return df_merged