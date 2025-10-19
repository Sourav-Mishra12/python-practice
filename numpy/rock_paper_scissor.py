import numpy as np
import matplotlib.pyplot as plt

def wins_count(rounds = 100 , seed = None):
    if seed is not None :
        np.random.seed(seed)
    
    player1 = np.random.randint(0,3,size=rounds)
    player2 = np.random.randint(0,3,size=rounds)

    ties = np.count_nonzero(player1 == player2)

    # 0 is rock ; 1 is paper ; 2 is scissor

    player1_wins = np.count_nonzero(       
        ((player1 == 0) & (player2 == 2)) |  # Rock beats Scissors
        ((player1 == 1) & (player2 == 0)) |  # Paper beats Rock
        ((player1 == 2) & (player2 == 1))    # Scissors beats Paper
    )

    player2_wins = rounds - (player1_wins - ties)

    return {
        "PLAYER 1 WINS ": player1_wins,
        "PLAYER 2 WINS ": player2_wins,
        "TIES" : ties,
        "TOTAL ROUNDS" : rounds
    }

results = wins_count()
print(results)


# Plot results
labels = list(results.keys())[:-1]  # exclude "Total Rounds"
values = list(results.values())[:-1]

plt.figure(figsize=(6,4))
plt.bar(labels, values, color=["blue", "red", "gray"])
plt.title("Rock-Paper-Scissors Simulation Results")
plt.ylabel("Number of Games")
plt.show()