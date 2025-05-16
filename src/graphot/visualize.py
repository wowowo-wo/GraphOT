'''
plot_graph_with_potentials:
Takes an adjacency matrix and Kantorovich potentials, then plots the graph and values of potentials using NetworkX and Matplotlib. Visualizes the flow of optimal transport."

plot_graph_with_transport:
Takes an adjacency matrix and a transport plan, then plots the graph with directed edges showing the transport flow using NetworkX and Matplotlib."
'''


import matplotlib.pyplot as plt
import networkx as nx

def plot_graph_with_potentials(adj_matrix, potential1, potential2):
    G = nx.from_numpy_array(adj_matrix)
    pos = nx.spring_layout(G, seed=5)

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=600, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray')

    for i in range(len(potential1)):
        plt.text(pos[i][0], pos[i][1] + 0.05, f"{potential1[i]:.2f}", ha='center', fontsize=14, fontweight='bold', color='blue')
        plt.text(pos[i][0], pos[i][1] - 0.05, f"{potential2[i]:.2f}", ha='center', fontsize=14, fontweight='bold', color='red')

    plt.title("Graph with Kantorovich potential", fontsize=14)
    plt.show()

def plot_graph_with_transport(adj_matrix,transport_plan):

    n = adj_matrix.shape[0]
    base_G = nx.from_numpy_array(adj_matrix)
    transport_G = nx.DiGraph()
    pos = nx.spring_layout(base_G, seed=5)

    transport_edges = []
    edge_labels = {}
    widths = []

    for i in range(n):
        for j in range(n):
            flow = transport_plan[i, j]
            if flow > 1e-6:
                transport_edges.append((i, j))
                edge_labels[(i, j)] = f"{flow:.2f}"
                widths.append(flow * 5)

    transport_G.add_edges_from(transport_edges)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(base_G, pos, node_size=600, node_color='skyblue')
    nx.draw_networkx_labels(base_G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(base_G, pos, style='dotted', edge_color='gray', width=1)
    nx.draw_networkx_edges(transport_G, pos, edgelist=transport_edges, width=widths,
                           edge_color='black', arrows=True)
    nx.draw_networkx_edge_labels(transport_G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

    plt.title("Graph with transport plan", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
