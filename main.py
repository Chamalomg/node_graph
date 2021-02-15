import networkx as nx
import matplotlib.pyplot as plt
from Machine import Machine
from Champ import Champ
import random
import json

PATH = 'data/champions.json'

# Nombre machines
N = 15
machines = [Machine('Node' + str(i), 'Réseau' + str(i)) for i in range(N)]
# print(machines[N // 2])

nodes = []

edges = []


def add_nodes_json(path):
    with open(path) as champs:
        data = json.load(champs)
        for new_champ in data:
            nodes.append(Champ(new_champ['name'], new_champ['cost'], new_champ['traits']))


def add_edges(nodes):
    n = len(nodes)
    for i in range(n):
        for j in range(n):
            if all([i != j, nodes[i].traits, (nodes[i], nodes[j]) not in edges]):
                L = [nodes[i].traits[k] == nodes[j].traits[l]
                       for k in range(len(nodes[i].traits)) for l in range(len(nodes[j].traits))]
                if any(L):
                    edges.append((nodes[i], nodes[j]))


def plot_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes), G.add_edges_from(edges)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    add_nodes_json(PATH)
    add_edges(nodes)
    plot_graph(nodes, edges)
    a = 1
