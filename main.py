import networkx as nx
import matplotlib.pyplot as plt

nodes = [
    (1, {"color": "red"}),
    (2, {"color": "green"}),
    (3, {"color": "green"}),
    (4, {"color": "green"}),
    (5, {"color": "green"}),
]

edges = [
    (1, 5),
    (1, 2),
    (2, 5),
    (4, 5),
    (2, 5),
    (3, 4),
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
print(list(G.nodes))
print(list(G.edges))


# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
