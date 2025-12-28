#Import Library
import math

#Define Variables
S0 = 500            # Current Stock Price
K = 300             # Strike Price
T = 1               # Time Period
r = 0.06            # Risk Free Rate
vol = 0.2           # Volatility

def norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def black_scholes_model(S0, K, T, r, vol, opttype = 'C'):

    d1 = (math.log(S0 / K) + (r + 0.5 * vol ** 2) * T)/(vol * math.sqrt(T))
    d2 = d1 - vol * math.sqrt(T)

    if opttype == 'C':
        price = S0 * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    else:
        price = K * math.exp(-r * T) * norm_cdf(-d2) - S0 * norm_cdf(-d1)

    return price

call_price = black_scholes_model(S0, K, T, r, vol, opttype = 'C' )
put_price = black_scholes_model(S0, K, T, r, vol, opttype = 'P' )

print(f'Call Price : {call_price}')
print(f'Put Price : {put_price}')
