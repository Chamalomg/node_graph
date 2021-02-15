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

traits = ['Boss', 'Cultist', 'Divine', 'Duelist', 'Emperor', 'Fortune', 'Keeper', 'Set4_Adept', 'Set4_Assassin',
          'Set4_Blacksmith', 'Set4_Brawler', 'Set4_Daredevil', 'Set4_Dragonsoul', 'Set4_Elderwood',
          'Set4_Enlightened', 'Set4_Executioner', 'Set4_Exile', 'Set4_Fabled', 'Set4_Mage', 'Set4_Mystic',
          'Set4_Ninja', 'Set4_Slayer', 'Set4_Spirit', 'Set4_Syphoner', 'Set4_Vanguard', 'Sharpshooter', 'Warlord']

traits_color = {key: i/27 for i, key in enumerate(traits)}


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
    node_color = [node.color for node in G.nodes()]
    print(node_color)
    nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=node_color, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    add_nodes_json(PATH)
    add_edges(nodes)
    plot_graph(nodes, edges)
