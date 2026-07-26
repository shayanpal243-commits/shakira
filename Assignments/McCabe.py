import networkx as nx
import matplotlib.pyplot as plt

print("McCabe Cyclomatic Complexity")

choice = input("1. Enter your own graph\n2. Use sample graph\nEnter choice: ")

edges = []

if choice == "1":
    print("Enter edges like 1,2")
    print("Type 'done' to finish")

    while True:
        edge = input("Edge: ")

        if edge.lower() == "done":
            break

        try:
            a, b = edge.split(",")
            edges.append((a.strip(), b.strip()))
        except:
            print("Invalid input")
else:
    edges = [
        ("1", "2"),
        ("2", "3"),
        ("2", "6"),
        ("3", "4"),
        ("3", "5"),
        ("4", "6"),
        ("5", "6"),
        ("6", "2"),
        ("6", "7")
    ]
    print("\nUsing sample graph")

if len(edges) == 0:
    print("No edges entered.")
    exit()

G = nx.DiGraph()
G.add_edges_from(edges)

E = G.number_of_edges()
N = G.number_of_nodes()

complexity = E - N + 2

decision_nodes = []

for node in G.nodes():
    if G.out_degree(node) >= 2:
        decision_nodes.append(node)

complexity2 = len(decision_nodes) + 1

print("\n----- RESULT -----")
print("Edges               :", E)
print("Nodes               :", N)
print("Decision Nodes      :", decision_nodes)
print("Cyclomatic (E-N+2)  :", complexity)
print("Cyclomatic (P+1)    :", complexity2)

if complexity <= 10:
    print("Risk Level          : Low")
elif complexity <= 20:
    print("Risk Level          : Moderate")
elif complexity <= 50:
    print("Risk Level          : High")
else:
    print("Risk Level          : Very High")

colors = []

for node in G.nodes():
    if node in decision_nodes:
        colors.append("orange")
    else:
        colors.append("lightblue")

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=colors,
    node_size=1000,
    arrows=True
)

plt.title("Control Flow Graph")
plt.show()