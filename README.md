## ✅ README.md – Trading Signal (Moving Average Crossover)

---

# 📈 Trading Signal – Moving Average Crossover

A Python script that downloads Apple (AAPL) stock data, calculates a user-defined Simple Moving Average (SMA), and generates Buy/Sell/Hold signals based on price proximity to the SMA.

---

## 📋 Program Flow

| Step | Action |
|:----:|--------|
| 1 | Read command-line arguments: `filename` and `period` |
| 2 | Delete existing CSV file (if any) |
| 3 | Download AAPL data from Yahoo Finance |
| 4 | Clean and format data |
| 5 | Save data to CSV |
| 6 | Calculate Moving Average (user-defined period) |
| 7 | Generate Buy/Sell/Hold signals |
| 8 | Print preview of results |

---

## 🧠 Key Code Concepts

| Concept | How it's used |
|---------|----------------|
| `sys.argv` | Read command-line arguments |
| `yfinance` | Download stock data |
| `df.columns.droplevel(1)` | Remove multi-index columns |
| `df.reset_index()` | Turn date index into column |
| `pd.to_numeric()` | Ensure Close is numeric |
| Manual MA calculation | Loop with `.iloc` slicing |
| Signal logic | Buy/Sell/Hold based on 1% threshold |
| `abs()` | Calculate absolute difference |

---

## 📊 Signal Logic

| Condition | Signal |
|-----------|--------|
| `abs(Close - MA) / MA <= 0.01` | **Hold** (within 1%) |
| `Close > MA` | **Buy** |
| `Close < MA` | **Sell** |

---

## 🖥️ Command-Line Usage

```bash
python trading_signal.py <filename> <period>
```

| Argument | Description | Example |
|----------|-------------|---------|
| `filename` | CSV file to save data | `data.csv` |
| `period` | Moving average window | `10` |

### Example
```bash
python trading_signal.py aapl_data.csv 10
```

---

## 📤 Output Examples

### Console Output
```
data.csv already exists. It has been removed to ensure fresh data.
data.csv not found. Downloading data...
[*********************100%***********************]  1 of 1 completed

Moving Average Period: 10
--------------------------------------------------

         Date   Close     MA Signal
0  2024-01-02  183.56    NaN   Hold
1  2024-01-03  182.19    NaN   Hold
2  2024-01-04  179.87    NaN   Hold
3  2024-01-05  179.15    NaN   Hold
4  2024-01-08  183.48    NaN   Hold
5  2024-01-09  183.07    NaN   Hold
6  2024-01-10  184.11    NaN   Hold
7  2024-01-11  183.51    NaN   Hold
8  2024-01-12  183.84    NaN   Hold
9  2024-01-16  181.57  182.95   Sell
10 2024-01-17  180.64  182.64   Sell
11 2024-01-18  186.52  183.67    Buy
12 2024-01-19  189.42  185.07    Buy
13 2024-01-22  191.72  186.81    Buy
14 2024-01-23  193.00  188.71    Buy
```

---

## ✅ Key Takeaways

| Concept | How it's used |
|---------|----------------|
| `sys.argv` | Accept filename and period from terminal |
| Manual MA | Loop-based calculation with variable window |
| `abs()` | Calculate percentage difference |
| 1% threshold | Determines Hold vs Buy/Sell |
| `df.iloc[]` | Slice Close prices for MA window |
| `df.loc[]` | Assign values to specific rows |

---

## 📁 Project Status

| Feature | Status |
|---------|--------|
| Command-line arguments | ✅ |
| Download data | ✅ |
| Save to CSV | ✅ |
| Calculate MA (variable period) | ✅ |
| Generate Buy/Sell/Hold signals | ✅ |
| Print preview | ✅ |
| Error handling | ✅ |

---

> *Last updated: May 2026*
```
