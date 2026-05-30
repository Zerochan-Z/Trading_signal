import pandas as pd
import yfinance as yf
import numpy as np
import os

file_name = 'signal_data.csv'

if os.path.exists(file_name):
    os.remove(file_name)
    print(f"{file_name} already exists. It has been removed to ensure fresh data.")

try:
    print(f"{file_name} not found. Downloading data...")
    df = yf.download('AAPL', start='2024-01-01', end='2024-06-01')
    df.columns = df.columns.droplevel(1)
    df.reset_index(inplace=True)

    df = df[['Date', 'Close']].copy()
    df.to_csv(file_name, index = False)
    print(f'Data saved. Shape: {df.shape}')
    
    df['Close'] = pd.to_numeric(df['Close']).round(4)

    df['MA'] = float('nan')
    for i in range(9,len(df)):
        window = df['Close'].iloc[i-9:i+1]
        df.loc[i, 'MA'] = window.mean().round(4)

    df['Signal'] = 'Hold'
    for i in range(9, len(df)):
        current_close = df.loc[i, 'Close']
        current_ma = df.loc[i, 'MA']
        
        if current_close > current_ma:
            df.loc[i, 'Signal'] = 'Buy'
        elif current_close < current_ma:
            df.loc[i, 'Signal'] = 'Sell'
        else:
            df.loc[i, 'Signal'] = 'Hold'

    print('\n' + '-'*50 + '\n')
    print(df[['Date', 'Close', 'MA', 'Signal']].head(15))

except Exception as e:
    print(f"An error occurred: {e}")