import numpy as np
import time
import matplotlib.pyplot as plt

np.random.seed(42)

array_sizes = [10_000, 100_000, 500_000, 1_000_000]
loop_times = []
numpy_times = []

for N in array_sizes:
    a = np.random.rand(N)
    b = np.random.rand(N)

    # Python loop
    start = time.time()
    dot_loop = 0
    for i in range(N):
        dot_loop += a[i] * b[i]
    loop_time = time.time() - start
    loop_times.append(loop_time)

    # NumPy dot
    start = time.time()
    dot_numpy = np.dot(a, b)
    numpy_time = time.time() - start
    numpy_times.append(numpy_time)

    # Print results
    print(f"Size {N:,}: Python loop = {loop_time:.4f}s, NumPy = {numpy_time:.6f}s")



plt.figure(figsize=(10,6))

plt.plot(array_sizes, loop_times, marker='o', color='red', label='Python Loop')
plt.plot(array_sizes, numpy_times, marker='o', color='blue', label='NumPy Vectorized')

plt.title("Python Loop vs NumPy Vectorization (Dot Product)")
plt.xlabel("Array Size")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()