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

# the utility function of a player
def UtilityMIS(targetNodeIndex):
    pass

# 1-1: create model of [ Maximal Independent Set (MIS) Game (Symmetric) ]
def CreateMISModel(graph, response):
    pass

# 1-2: create model of [ Asymmetric MDS-based IDS Game ]
def CreateAMDSIDSModel():
    pass

# 2: Maximum Matching Problem
def MaximumMatchingProblem():
    pass

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
    # get result of 1-1
    print(graph)
    print(response)
    CreateMISModel(graph, response)