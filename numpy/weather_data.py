import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

mean_temp = 20
temp_std = 5
days = 365

temps= np.random.normal(mean_temp,temp_std , days)
rounded_temp = np.ceil(temps)
#print("first 10 days temp :" , rounded_temp)

hottest = max(rounded_temp)
coldest  = min(rounded_temp)

print("HOTTEST TEMP :" , hottest)
print("COLDEST TEMP :" , coldest)

hottest_day = np.argmax(rounded_temp)+1
coldest_day = np.argmin(rounded_temp)+1

print("HOTTEST DAY : ", hottest_day)
print("COLDEST DAY : ", coldest_day)

temps_trimmed = temps[:360]

temps_reshaped = temps_trimmed.reshape(12,30)

monthly_avg = temps_reshaped.mean(axis=1)
monthly_avg_rnd =np.ceil(monthly_avg)
print("MONTHLY AVERAGE : ", monthly_avg_rnd)

# Plotting daily temperatures
plt.figure(figsize=(12,5))
plt.plot(rounded_temp, color='skyblue', label='Daily Temperature')
plt.title("Daily Temperatures Over the Year")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()

# Plotting monthly averages
months = np.arange(1, 13)
plt.figure(figsize=(10,5))
plt.bar(months, monthly_avg_rnd, color='orange', edgecolor='black')
plt.title("Monthly Average Temperatures")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.xticks(months)
plt.show()