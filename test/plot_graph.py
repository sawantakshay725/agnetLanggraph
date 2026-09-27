import matplotlib.pyplot as plt
import networkx as nx

from graph.graph import build_supply_chain_graph

def plot_supply_chain_graph():
    # Build the graph (uncompiled version so we can inspect)
    builder = build_supply_chain_graph().builder if hasattr(build_supply_chain_graph(), "builder") else None
    
    # If builder not accessible, fallback: manually reconstruct edges
    # For now, we’ll just hardcode edges from your graph.py
    edges = [
        ("START", "demand_agent"),
        ("START", "inventory_agent"),
        ("START", "supplier_agent"),
        ("demand_agent", "analysis_agent"),
        ("inventory_agent", "analysis_agent"),
        ("supplier_agent", "analysis_agent"),
        ("analysis_agent", "validation_agent"),
        ("validation_agent", "analysis_agent"),  # loop
        ("validation_agent", "finish"),
        ("finish", "END"),
    ]

    nodes = set([n for e in edges for n in e])

    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # Layout and draw
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 6))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="lightblue",
        node_size=2500,
        font_size=10,
        font_weight="bold",
        arrows=True,
        arrowstyle="->",
        arrowsize=15
    )
    plt.title("Supply Chain LangGraph Dataflow", fontsize=14)
    plt.tight_layout()
    plt.savefig("test/supply_chain_graph.png")
    plt.show()

if __name__ == "__main__":
    plot_supply_chain_graph()
