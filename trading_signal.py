import sys
import pandas as pd
import yfinance as yf
import os

file_name = sys.argv[1]
period = int(sys.argv[2])

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
    
    df['Close'] = pd.to_numeric(df['Close']).round(4)

    df['MA'] = float('nan')
    for i in range(period -1, len(df)):
        df.loc[i, 'MA'] = df['Close'].iloc[i - period +1 : i+1].mean().round(4)

    df['Signal'] = 'Hold'
    for i in range(period -1, len(df)):
        diff = abs(df.loc[i, 'Close'] - df.loc[i, 'MA']) / df.loc[i,'MA']
        if diff <= 0.01:
            df.loc[i, 'Signal'] = 'Hold'
        elif df.loc[i, 'Close'] > df.loc[i, 'MA']:
            df.loc[i, 'Signal'] = 'Buy'
        else:
            df.loc[i, 'Signal'] = 'Sell'
    
    print(f'\nMoving Average Period: {period}')
    print('\n' + '-'*50 + '\n')
    print(df[['Date', 'Close', 'MA', 'Signal']].head(15))

except Exception as e:
    print(f"An error occurred: {e}")