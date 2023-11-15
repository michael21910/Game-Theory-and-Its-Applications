# WS model
import matplotlib.pyplot as plt
import random

# create a ring lattice
def createRingLattice(n, k):
    ringLattice = {}
    for i in range(n):
        ringLattice[i] = set()
        for j in range(i - k // 2, i):
            ringLattice[i].add(j % n)
        for j in range(i + 1, i + 1 + k // 2):
            ringLattice[i].add(j % n)
    return ringLattice

# create a WS model
def createWSModel(n, k, p):
    ring_lattice = createRingLattice(n, k)
    for i in range(n):
        for j in range(i + 1, i + 1 + k // 2):
            if random.random() < p:
                ring_lattice[i].remove(j % n)
                ring_lattice[i].add(random.randint(0, n - 1))
    return ring_lattice

# 1-1: create model of [ Maximal Independent Set (MIS) Game (Symmetric) ]
def createMISModel(n, k, p):
    pass

# 1-2: create model of [ Asymmetric MDS-based IDS Game ]
def createAMDSIDSModel(n, k, p):
    pass

# 2: Maximum Matching Problem
def maximumMatchingProblem(n, k, p):
    pass