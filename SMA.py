import statistics as st

def calculate_sma(n):
    prices = n
    
    size = 5
    sma_results = [None] * size
    
    for i in range(size, len(prices)):
        history = prices[i-size:i]
        sma = st.mean(history)
        sma_results.append(sma)
    
    return sma_results