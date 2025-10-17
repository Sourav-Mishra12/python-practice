import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
initial_price = 100
days = 100
num_stocks = 5

mean_return = 0.001
volatility = 0.02

daily_returns = np.random.normal(mean_return , volatility , (days,num_stocks))
print(daily_returns[:5])

price_series = np.zeros_like(daily_returns)
price_series[0] = initial_price*(1+daily_returns[0])

for t in range(1,days):
    price_series[t] = price_series[t-1]*(1+daily_returns[t])

plt.figure(figsize=(13,7))
for i in range(num_stocks):
    plt.plot(price_series[:,i] , label= f"STOCK {i+1}")

plt.title("SIMULATED STOCK PRICE (RANDOM WALK)")
plt.xlabel("DAY")
plt.ylabel("PRICE")
plt.legend()
plt.show()