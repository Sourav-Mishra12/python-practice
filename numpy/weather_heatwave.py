import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)


temps = np.random.randint(23,45 , size= 30)

print(" DAILY TEMPRATURE FOR 30 DAYS :", temps)

heatwave_days = temps[temps > 30 ]

print("HEATWAVE DAYS IN THIS MONTH (TEMP > 30) : ",heatwave_days)

num_heatwave = np.count_nonzero(heatwave_days)
print("NUMBER OF HEATWAVE DAYS : " , num_heatwave)

heatwave_mask = temps > 30  # made for np.where as it only reads the boolean values

plt.figure(figsize=(11,4))

colors = np.where(heatwave_mask , 'red' , 'skyblue')

plt.bar(np.arange(1, 31), temps, color=colors)
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperatures with Heatwave Days Highlighted(In Blue)")
plt.xticks(np.arange(1, 31))
plt.show()