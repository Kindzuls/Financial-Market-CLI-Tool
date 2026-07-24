import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import sys
from import_finance import finance_market_shares
from MAD import calculate_mad
from SMA import calculate_sma
from RSI import calculate_rsi
import os


def main():
    if len(sys.argv) != 4:
        path = os.path.join('text','usage.txt')
        with open(path, 'r') as file:
            sys.exit(file.read().strip())
    
    ticker = sys.argv[1].upper()
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    
    if not ticker.strip():
        sys.exit('Invalid ticker format')
    
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        sys.exit('Not correct date')
        
    dates, prices = finance_market_shares(ticker, start_date, end_date)
    
    mads, lower, upper, anomalies = calculate_mad(prices)
    sma_results = calculate_sma(prices)
    rsi_results = calculate_rsi(prices)
    
    
    ## visualization
    dates = mdates.date2num(dates)
    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8), sharex=True)
    
    # upper graph with stock, prices, SMA and MAD
    ax1.plot(dates, prices, label=f'{ticker} price', color='blue', alpha=0.6)
    ax1.plot(dates, sma_results, label='SMA', color='orange', linestyle='--')
    
    ax1.scatter(dates, anomalies, color='red', label='Anomalies (MAD)', zorder=5)
    
    ax1.plot(dates, upper, color='red', linestyle=':', alpha=0.4, label='MAD Upper Bound')
    ax1.plot(dates, lower, color='red', linestyle=':', alpha=0.4, label='MAD Lower Bound')
    
    ax1.set_title(f'{ticker} shares analysis (SMA & MAD)')
    ax1.set_ylabel('Price ($)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    
    #lower  graph (RSI)
    ax2.plot(dates, rsi_results, label='RSI (14)', color='purple')
    
    ax2.axhline(70, color='red', linestyle=':', alpha=0.7, label='Overbought (70)')
    ax2.axhline(30, color='green', linestyle=':', alpha=0.7, label='Oversold (30)')
    
    ax2.fill_between(dates, 30, 70, color='purple', alpha=0.05)
    
    ax2.set_title('Relative Strenght Index (RSI)')
    ax2.set_ylabel('Value of RSI')
    ax2.set_ylim(0,100)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    locator = mdates.AutoDateLocator()
    ax2.xaxis.set_major_locator(locator)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
    fig.autofmt_xdate()
    plt.tight_layout()
    
    plt.show()

if __name__ == '__main__':
    main()