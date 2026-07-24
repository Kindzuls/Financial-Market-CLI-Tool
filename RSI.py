import statistics as st

def calculate_rsi(n):
    prices = n
    
    size = 14
    rsi_results = [None] * size
    
    for i in range(size, len(prices)):
        
        history = prices[i - size: i+1]
        
        gains = []
        loses = []
        
        for c in range(1, len(history)):
            delta = history[c] - history[c-1]
            
            if delta > 0:
                gains.append(delta)
            elif delta < 0:
                delta = abs(delta)
                loses.append(delta)
            else:
                gains.append(delta)
                loses.append(delta)
        
        avg_gains = st.mean(gains)
        avg_loses = st.mean(loses)
        
        if avg_loses == 0:
            rsi = 100
        else:
            rs = avg_gains / avg_loses
            rsi = 100 - (100/(1+rs))
            
        rsi_results.append(rsi)
    
    return rsi_results
