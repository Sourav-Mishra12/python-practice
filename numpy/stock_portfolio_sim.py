import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

num_stocks = 5
days = 252
initial_price = 100
mean_return = 0.0005
volatility = 0.02

daily_returns = np.ceil(np.random.normal(mean_return,volatility,(days,num_stocks)))

prices  = np.zeros_like(daily_returns)

prices[0] = initial_price * (1 + daily_returns[0])

for i in range(1,days):
     prices[i] = prices[i-1] * (1 + daily_returns[i])


weights = np.array([1/num_stocks] * num_stocks)

portfolio_values = prices @ weights

total_return = (portfolio_values[-1] - portfolio_values[0]) / portfolio_values[0]

print(f"Total Portfolio Return: {total_return*100:.2f}%")

# PLOTTING CHARTS

plt.figure(figsize=(13,7))
for i in range(num_stocks):
    plt.plot(prices[:, i], label=f'Stock {i+1}')

plt.plot(portfolio_values, color='black', linewidth=2.5, label='Portfolio Value')
plt.title("Stock Portfolio Simulation")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()
