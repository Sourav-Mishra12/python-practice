import numpy as np


magnitudes = np.array([
    2.1, 2.5, 2.7, 3.0, 3.2, 3.5, 3.8, 4.0, 4.2, 4.5,
    4.7, 5.0, 5.3, 5.5, 5.8, 6.0, 6.3, 6.5, 6.8, 7.0
])


count = len(magnitudes)
min_mag = np.min(magnitudes)
max_mag = np.max(magnitudes)
mean_mag = np.mean(magnitudes)
median_mag = np.median(magnitudes)
std_mag = np.std(magnitudes)

print("Number of earthquakes:", count)
print("Minimum magnitude:", min_mag)
print("Maximum magnitude:", max_mag)
print("Mean magnitude:", mean_mag)
print("Median magnitude:", median_mag)
print("Standard deviation:", std_mag)

# --- Frequency Distribution (Histogram) ---
# bins = ranges: 2-3, 3-4, 4-5, 5-6, 6-7
hist, bins = np.histogram(magnitudes, bins=np.arange(2, 8, 1))

print("\nHistogram counts:", hist)
print("Bin edges:", bins)
