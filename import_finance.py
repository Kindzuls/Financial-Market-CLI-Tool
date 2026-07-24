import yfinance as yf
import sys

def finance_market_shares(ticker, start_date, end_date):
    try:
        
        data = yf.download(ticker, start=start_date, end=end_date)
        
        if data.empty:
            raise ValueError
        
        dates = data.index.strftime('%Y-%m-%d').tolist()
        prices = data['Close'].values.flatten().tolist()
        
        return dates, prices
        
    except ValueError:
        sys.exit('Error while donwloading')

