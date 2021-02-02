import networkx as nx
import matplotlib.pyplot as plt
from Machine import Machine
import random

# Nombre machines
N = 15
machines = [Machine('Node' + str(i), 'Réseau' + str(i)) for i in range(N)]
print(machines[N//2])

nodes = [
    (machines[i], {"color": "red"}) for i in range(N)
]

edges = [
    (machines[random.randint(0, N-1)], machines[random.randint(0, N-1)]) for i in range(5*N)
]

G = nx.Graph()
G.add_nodes_from(nodes), G.add_edges_from(edges)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
