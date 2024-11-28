import networkx as nx
import matplotlib.pyplot as plt

# Definir el grafo
graph = {
    "A": [("B", 8), ("C", 7)],
    "B": [("D", 9)],
    "C": [("E", 9), ("F", 6)],
    "D": [("G", 0), ("H", 1)],
    "F": [("H", 1), ("I", 0)],
    "E": [],
    "G": [],
    "H": [],
    "I": []
}

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos y aristas al grafo
for node, edges in graph.items():
    for edge in edges:
        G.add_edge(node, edge[0], weight=edge[1])

# Definir posiciones estáticas para los nodos
pos = {
    "A": (0, 0),
    "B": (1, 1),
    "C": (1, -1),
    "D": (2, 1),
    "E": (2, -2),
    "F": (2, 0),
    "G": (3, 1),
    "H": (3, 0),
    "I": (3, -1)
}

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="pink", font_size=15, font_weight="bold", arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Mostrar el grafo
plt.show()