import numpy as np

def dice_roll(rolls = 1000 , seed = None ):
    if seed is not None:
        np.random.seed(seed)

    die1 = np.random.randint(1,7,size=rolls)
    die2 = np.random.randint(1,7,size=rolls)

    sums = die1 + die2

    counts = np.bincount(sums)[2:]

    return counts , sums

counts , sums = dice_roll()
print("The count for sums 2-12 : " , counts)