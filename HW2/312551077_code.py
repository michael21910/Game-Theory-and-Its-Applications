# WS model
import matplotlib.pyplot as plt
import random

# create a ring lattice
def create_ring_lattice(n, k):
    ring_lattice = {}
    for i in range(n):
        ring_lattice[i] = set()
        for j in range(i - k // 2, i):
            ring_lattice[i].add(j % n)
        for j in range(i + 1, i + 1 + k // 2):
            ring_lattice[i].add(j % n)
    return ring_lattice

# create a WS model
def create_WS_model(n, k, p):
    ring_lattice = create_ring_lattice(n, k)
    for i in range(n):
        for j in range(i + 1, i + 1 + k // 2):
            if random.random() < p:
                ring_lattice[i].remove(j % n)
                ring_lattice[i].add(random.randint(0, n - 1))
    return ring_lattice

WSModel = create_WS_model(20, 4, 0.1)
print(WSModel)