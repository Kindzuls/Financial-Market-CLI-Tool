import statistics as st

def calculate_mad(n):
    prices = n
    
    size = 5
    
    mads = [None] * size
    upper = [None] * size
    lower = [None] * size
    anomalies = [None] * size
    
    for i in range(size, len(prices)):
        history = prices[i-size:i]
        med = st.median(history)
        devetation = [abs(x-med) for x in history]
        mad = st.median(devetation)
        
        mads.append(mad)
        
        up = med + 2*mad
        low = med - 2*mad
        
        upper.append(up)
        lower.append(low)
        
        current_price = prices[i]
        if current_price > up or current_price < low:
            anomalies.append(current_price)
        else:
            anomalies.append(None)
        
    return mads, lower, upper, anomalies