import numpy as np
import matplotlib.pyplot  as ply


rolls = np.random.randint(1,7, size = 1000)

values , counts = np.unique(rolls,return_counts=True)

print("VALUES :",values)
print("COUNTS : ",counts)

probabilities = counts / counts.sum()
print("probabilities : ",probabilities)

ply.bar(values,counts , tick_label = values)
ply.title ("DICE ROLL FREQUENCIES (1000 DICES)")
ply.xlabel("DIE FACE")
ply.ylabel("FREQUENCIES")
ply.show()