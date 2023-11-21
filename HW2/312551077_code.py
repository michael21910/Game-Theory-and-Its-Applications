import random

# the best response of a player in the Maximal Independent Set (MIS) Game (Symmetric)
def BestResponseMIS(targetNodeIndex):
    # graph[targetNodeIndex] are the open neighbors
    for i in range(len(graph[targetNodeIndex])):
        if response[graph[targetNodeIndex][i]] == 1:
            response[targetNodeIndex] = 0
            return
    response[targetNodeIndex] = 1
    return

# determine the player should change strategy or not according to the utility function of a player
def UtilityMIS(targetNodeIndex):
    # graph[targetNodeIndex] are the open neighbors
    alpha = 1000
    openNeighborInGameCounter = 0
    for i in range(len(graph[targetNodeIndex])):
        if response[graph[targetNodeIndex][i]] == 1:
            openNeighborInGameCounter += 1
    utilityTargetInGame = 1 - alpha * openNeighborInGameCounter
    # if the player is in the game but the utility is lower than the player not in the game, change strategy
    if response[targetNodeIndex] == 1 and utilityTargetInGame < 0:
        return True
    # if the player is not in the game but the utility is higher than the player not in the game, change strategy
    elif response[targetNodeIndex] == 0 and utilityTargetInGame > 0:
        return True
    return False

# determine if the game is in Nash Equilibrium (MIS)
def IsNashEquilibriumMIS():
    improveList = list()
    for i in range(len(graph) - 1):
        improveList.append(UtilityMIS(i + 1))
    for i in range(len(improveList)):
        if improveList[i] == True:
            return False
    return True

# 1-1: create model of [ Maximal Independent Set (MIS) Game (Symmetric) ]
def CreateMISModel(graph, response):
    # randomize initial response
    for i in range(len(response)):
        response[i] = random.randint(0, 1)
    while IsNashEquilibriumMIS() == False:
        for i in range(len(graph) - 1):
            BestResponseMIS(i + 1)
    return response[1:]    

# get Gi(C) of the player
def GofAMDSIDS(targetNodeIndex):
    # alpha is a constant greater than 1
    alpha = 10
    InGameCounter = 0
    if response[targetNodeIndex] == 1:
        InGameCounter += 1
    for i in range(len(graph[targetNodeIndex])):
        if response[graph[targetNodeIndex][i]] == 1:
            InGameCounter += 1
    return alpha if InGameCounter == 1 else 0

# get Wi(C) of the player
def WofAMDSIDS(targetNodeIndex):
    gamma = 1000
    W = 0
    for i in range(len(graph[targetNodeIndex])):
        if len(graph[targetNodeIndex]) < len(graph[graph[targetNodeIndex][i]]):
            W += response[graph[targetNodeIndex][i]] *  response[targetNodeIndex] * gamma
    return W

# get the utility of the player
def UtilityAMDSIDS(targetNodeIndex):
    beta = 5
    utility = GofAMDSIDS(targetNodeIndex)
    for i in range(len(graph[targetNodeIndex])):
        utility += GofAMDSIDS(graph[targetNodeIndex][i])
    utility -= beta
    utility -= WofAMDSIDS(targetNodeIndex)
    return True if utility < 0 else False

# determine if the game is in Nash Equilibrium (AMDSIDS)
def IsNashEquilibriumAMDSIDS():
    improveList = list()
    for i in range(len(graph) - 1):
        improveList.append(UtilityAMDSIDS(i + 1))
    for i in range(len(improveList)):
        if improveList[i] == True:
            return False
    return True

# 1-2: create model of [ Asymmetric MDS-based IDS Game ]
def CreateAMDSIDSModel(graph, response):
    # randomize initial response
    for i in range(len(response)):
        response[i] = random.randint(0, 1)
    while IsNashEquilibriumAMDSIDS() == False:
        for i in range(len(graph) - 1):
            if UtilityAMDSIDS(i + 1) == True:
                response[i + 1] = 1 - response[i + 1]
    return response[1:]

# 2: Maximum Matching Problem
def MaximumMatchingProblem(graph, response):
    pass

# reset response to 0
def ResetResponse(response):
    for i in range(len(response)):
        response[i] = 0

if __name__ == "__main__":
    # read input
    info = input().split(" ")
    # relationship of nodes (no node 0)
    graph = [[]]
    # response of each node
    response = [0]
    # go through information
    for i in range(int(info[0]) + 1):
        if i == 0:
            continue
        nodeConnection = list()
        for j in range(int(info[0])):
            if info[i][j] == "1":
                nodeConnection.append(j + 1)
        graph.append(nodeConnection)
        response.append(0)

    print("Graph connection information:", graph, sep="\n", end="\n\n")

    # get result of 1-1
    ResetResponse(response)
    print("1-1 response:", CreateMISModel(graph, response))

    # get result of 1-2
    ResetResponse(response)
    print("1-2 response:", CreateAMDSIDSModel(graph, response))

    # get result of 2
    ResetResponse(response)
    MaximumMatchingProblem(graph, response)