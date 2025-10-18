import numpy as np
import matplotlib.pyplot as plt
import time

np.random.seed(42)

N = 10_00_000
data1 = np.random.rand(N)
data2 = np.random.rand(N)

# DOING ADDITION USING PYTHON LOOPS

start_time = time.time()
result = []

for i in range (N):
    result.append(data1[i] + data2[i])
loop_time = time.time() - start_time

print(f"THE TIME TAKEN FOR THE COMPUTATION USING PYTHON LOOP IS : {loop_time:.4f} seconds")

# DOING THE COMPUTATION USING VECTORIZATION

start_time_vector = time.time()
vector_result = data1 + data2
loop_time_vector = time.time() - start_time_vector
print(f"THE TIME TAKEN FOR THE COMPUTATION USING VECTORIZATION IS : {loop_time_vector:.4f} seconds")

# MATCHING THE RESULTS

if np.allclose(result , vector_result):
    print("RESULTS ARE MATCHING")
else:
    print("RESULTS DID NOT MATCH")

# DIFFERENCE OF TIME BETWEEN BOTH OF THE APPROACHES

diff = loop_time / loop_time_vector
print(f"VECTORS ARE {diff:.1f} times faster than Python loops")

# PLOTTING THE RESULTS

plt.bar(["PYTHON LOOP" , "NUMPY VERCOTRIZED"],
[loop_time , loop_time_vector] , color = ["red" , "blue"])
plt.title("PERFORMANCE COMAPRISION : LOOP vs VECTORIZED")
plt.ylabel("EXECUTION TIME IN SECONDS")
plt.show()