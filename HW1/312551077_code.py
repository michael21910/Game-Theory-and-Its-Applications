# fictitious play implementation
import numpy as np
import matplotlib.pyplot as plt

# input payoff matrix
payoffMatrix = input("""
Please input payoff matrix row by row.
Example(prisoner's dilemma): (-1, -1), (-3, 0), (0, -3), (-2, -2)
""")

# parse payoff matrix
payoffMatrix = payoffMatrix.replace('(', '').replace(')', '').replace(' ', '').split(',')
payoffMatrix = [int(i) for i in payoffMatrix]
payoffMatrix = np.array(payoffMatrix).reshape(-1, 2)

# set up iterations
iterations = 3000

# initial state
initialStrategyProfiles = ['(1, 1)', '(1, 2)', '(2, 1)', '(2, 2)']

# store strategy profiles for displaying
strategyProfiles = []

# set up figure size
plt.figure(figsize=(16, 8))

# play game
for count, initialStrategyProfile in enumerate(initialStrategyProfiles):
    # player A belief means the player b's history, vice versa
    playerABelief = [0, 0]
    playerBBelief = [0, 0]
    playerAPayoff = [0, 0]
    playerBPayoff = [0, 0]
    StrategyProfileResult = []
    for i in range(iterations):
        aChoice = 0
        bChoice = 0
        if i == 0:
            # parse initial state
            initialStrategyProfile = initialStrategyProfile.replace('(', '').replace(')', '').replace(' ', '').split(',')
            if initialStrategyProfile[0] == '1':
                playerBBelief[0] += 1
                aChoice = 1
            else:
                playerBBelief[1] += 1
                aChoice = 2
            if initialStrategyProfile[1] == '1':
                playerABelief[0] += 1
                bChoice = 1
            else:
                playerABelief[1] += 1
                bChoice = 2
        else:
            # update belief
            if playerAPayoff[0] > playerAPayoff[1]:
                playerBBelief[0] += 1
                aChoice = 1
            elif playerAPayoff[0] < playerAPayoff[1]:
                playerBBelief[1] += 1
                aChoice = 2
            else:
                aRandomChoice = np.random.randint(1, 2)
                playerBBelief[aRandomChoice - 1] += 1
                aChoice = aRandomChoice
            if playerBPayoff[0] > playerBPayoff[1]:
                playerABelief[0] += 1
                bChoice = 1
            elif playerBPayoff[0] < playerBPayoff[1]:
                playerABelief[1] += 1
                bChoice = 2
            else:
                bRandomChoice = np.random.randint(1, 2)
                playerABelief[bRandomChoice - 1] += 1
                bChoice = bRandomChoice
        # player A payoff
        playerAPayoff[0] = playerABelief[0] * payoffMatrix[0][0] + playerABelief[1] * payoffMatrix[1][0]
        playerAPayoff[1] = playerABelief[0] * payoffMatrix[2][0] + playerABelief[1] * payoffMatrix[3][0]
        # player B payoff
        playerBPayoff[0] = playerBBelief[0] * payoffMatrix[0][1] + playerBBelief[1] * payoffMatrix[2][1]
        playerBPayoff[1] = playerBBelief[0] * payoffMatrix[1][1] + playerBBelief[1] * payoffMatrix[3][1]
        # Combine strategy profiles into a single integer
        # A1B1 = 1, A1B2 = 2, A2B1 = 3, A2B2 = 4
        strategy_profile = aChoice * 2 + bChoice - 2
        StrategyProfileResult.append(strategy_profile)
    strategyProfiles.append(StrategyProfileResult)

    # Create subplots
    plt.subplot(2, 2, count + 1)
    y_ticks = [1, 2, 3, 4]
    playerStrategyProfile = ["(r1, c1)", "(r1, c2)", "(r2, c1)", "(r2, c2)"]
    plt.plot(range(1, 1 + iterations), strategyProfiles[count], marker='o', markersize=0.75)
    xlabel = plt.xlabel(f'P(r*), P(c*): ({playerBBelief[0] / iterations:.4f}, \
{playerBBelief[1] / iterations:.4f}), \
({playerABelief[0] / iterations:.4f}, \
{playerABelief[1] / iterations:.4f})'
    )
    xlabel.set_color('red')
    plt.ylabel('Strategy Profile (Combined)')
    plt.gca().set_yticks(y_ticks)
    plt.gca().set_yticklabels(playerStrategyProfile)
    # plt.title(f'Initial Strategy Profile: {initialStrategyProfile}')
    plt.title(f'Starts from strategy profile: {playerStrategyProfile[count]}')

plt.tight_layout()
plt.show()