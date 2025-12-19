# Import Library
import numpy as np

# Define Variables
S0 = 100
K = 100
T = 1
r = 0.06
N = 3
u = 1.1
d = 1/u
opttype = 'C'

def european_binomial_option_price(S0, K, T, r, N, u, d, opttype = 'C'):
    dt = T/N
    p = (np.exp(r*dt) - d)/(u - d)
    disc = np.exp(-r * dt)

    S = np.zeros(N + 1)

    S[0] = S0 * (d ** N)
    for j in range (1, N+1):
        S[j] = S[j-1] * (u/d)

    C = np.zeros(N + 1)
    if opttype == 'C':
        for j in range (0, N + 1):
            C[j] = max(S[j] - K, 0)
    else:
        for j in range (N + 1):
            C[j] = max(K - S[j], 0)

    for i in range (N, 0, -1):
        for j in range (i):
            C[j] = disc * (p * C[j + 1] + (1 - p) * C[j])

    return C[0]

call_price = european_binomial_option_price(S0, K, T, r, N, u, d, 'C')
put_price  = european_binomial_option_price(S0, K, T, r, N, u, d, 'P')

print(f'Call Price: {call_price}')
print(f'Put Price: {put_price}')

