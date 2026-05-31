# Trading_signal
Last project before orientation day comes. (‾◡◝)

---

## 📁 Part 1: Imports & Setup

| Code | Description |
|------|-------------|
| `import sys` | Access command‑line arguments |
| `import pandas as pd` | Data manipulation toolkit |
| `import yfinance as yf` | Download stock data |
| `import os` | File and operating system tools |

---

## 🔧 Part 2: Command Line Arguments

| Code | Description |
|------|-------------|
| `sys.argv[1]` | First argument after script name (filename) |
| `sys.argv[2]` | Second argument after script name (MA period) |
| `int(sys.argv[2])` | Convert period argument to integer |

---

## 📥 Part 3: File Handling

| Code | Description |
|------|-------------|
| `os.path.exists(file_name)` | Check if file already exists |
| `os.remove(file_name)` | Delete existing file |
| `df.to_csv(file_name, index=False)` | Save DataFrame to CSV without row numbers |

---

## 🎨 Part 4: Data Download & Cleaning

| Code | Description |
|------|-------------|
| `yf.download('AAPL', start, end)` | Download Apple stock data |
| `df.columns.droplevel(1)` | Remove ticker level from column headers |
| `df.reset_index(inplace=True)` | Turn date index into a regular column |
| `df[['Date', 'Close']].copy()` | Keep only Date and Close columns |

---

## 🔀 Part 5: Data Type Conversion

| Code | Description |
|------|-------------|
| `pd.to_numeric(df['Close'])` | Convert Close column from string to number |
| `.round(4)` | Round to 4 decimal places |

---

## 🔁 Part 6: Moving Average Calculation (Loop)

| Code | Description |
|------|-------------|
| `df['MA'] = float('nan')` | Create empty MA column filled with NaN |
| `range(period - 1, len(df))` | Loop from index (period-1) to end |
| `df['Close'].iloc[start:end]` | Select window of Close prices by position |
| `.mean()` | Calculate average of selected window |
| `df.loc[i, 'MA'] = value` | Store MA value at row i |

---

## 📦 Part 7: Signal Generation

| Code | Description |
|------|-------------|
| `df['Signal'] = 'Hold'` | Create Signal column, default to Hold |
| `abs(Close - MA) / MA` | Calculate percentage difference |
| `diff <= 0.01` | Check if within 1% of MA |
| `Close > MA` | Check if Close above MA |
| `df.loc[i, 'Signal'] = 'Buy'` | Assign Buy signal |
| `df.loc[i, 'Signal'] = 'Sell'` | Assign Sell signal |
| `df.loc[i, 'Signal'] = 'Hold'` | Assign Hold signal |

---

## 📤 Part 8: Output Display

| Code | Description |
|------|-------------|
| `print(f'\nMoving Average Period: {period}')` | Show MA period used |
| `print('-'*50)` | Print separator line |
| `df[['Date', 'Close', 'MA', 'Signal']].head(15)` | Select columns and show first 15 rows |

---

## ⚙️ Part 9: Error Handling

| Code | Description |
|------|-------------|
| `try:` | Attempt to run code block |
| `except Exception as e:` | Catch any error that occurs |
| `print(f"An error occurred: {e}")` | Display error message |

---

## 📊 Summary Table (Part by Part)

| Part | Section | Purpose |
|------|---------|---------|
| 1 | Imports | Load required libraries |
| 2 | Command Line Arguments | Get filename and MA period from user |
| 3 | File Handling | Delete old file, save new data |
| 4 | Data Download & Cleaning | Get AAPL data, clean structure |
| 5 | Data Type Conversion | Ensure Close is numeric |
| 6 | Moving Average Calculation | Compute MA using loop |
| 7 | Signal Generation | Buy/Sell/Hold based on 1% threshold |
| 8 | Output Display | Print preview of results |
| 9 | Error Handling | Catch and display errors |

---

## ✅ One Sentence Summary

**The script imports libraries, reads filename and MA period from command line, downloads and cleans AAPL data, calculates moving average with a loop, generates Buy/Sell/Hold signals using a 1% threshold, and prints a preview – with error handling throughout.**
