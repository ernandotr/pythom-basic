import networkx as nx
import matplotlib.pyplot as plt

def create_brain_connectome():
    G = nx.random_geometric_graph(50, 0.3)
    plt.figure(figsize=(8, 8))
    nx.draw(G, node_size=50, node_color='blue', edge_color='gray')
    plt.title("Brain Connectome Visualization")
    plt.show()

create_brain_connectome()