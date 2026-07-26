import ast
import networkx as nx
import matplotlib.pyplot as plt


with open("path_testing/input.py", "r") as f:
    code = f.read()

tree = ast.parse(code)



decision_count = 0
conditions = []


def extract_conditions(node):
    global decision_count

    for child in ast.iter_child_nodes(node):

        if isinstance(child, ast.If):

            decision_count += 1
            conditions.append(ast.unparse(child.test))

        extract_conditions(child)


extract_conditions(tree)

cyclomatic_complexity = decision_count + 1


paths = []

if decision_count == 2:

    c1 = conditions[0]
    c2 = conditions[1]

    paths.append(
        f"Start -> IF({c1}) TRUE -> End"
    )

    paths.append(
        f"Start -> IF({c1}) FALSE -> IF({c2}) TRUE -> End"
    )

    paths.append(
        f"Start -> IF({c1}) FALSE -> IF({c2}) FALSE -> End"
    )


print("PATH TESTING ANALYSIS :-")

print(f"\nDecision Nodes = {decision_count}")

print(
    f"Cyclomatic Complexity = {cyclomatic_complexity}"
)

print("\nIndependent Paths:\n")

for i, p in enumerate(paths, start=1):

    print(f"Path {i}")
    print(p)
    print()


print("\nExecuting Program...\n")

EXECUTED_PATH = []

exec_globals = {
    "EXECUTED_PATH": EXECUTED_PATH
}

exec(code, exec_globals)

print("\nExecuted Branch:")

if EXECUTED_PATH:
    print(EXECUTED_PATH[0])


G = nx.DiGraph()

G.add_edge("Start", c1)

G.add_edge(c1, "Positive Path")
G.add_edge(c1, c2)

G.add_edge("Positive Path", "End")

G.add_edge(c2, "Negative Path")
G.add_edge(c2, "Zero Path")

G.add_edge("Negative Path", "End")
G.add_edge("Zero Path", "End")

pos = {
    "Start": (0, 5),

    c1: (0, 4),

    "Positive Path": (-2, 3),

    c2: (2, 3),

    "Negative Path": (1, 2),
    "Zero Path": (3, 2),

    "End": (0, 1)
}


edge_labels = {
    (c1, "Positive Path"): "TRUE",
    (c1, c2): "FALSE",

    (c2, "Negative Path"): "TRUE",
    (c2, "Zero Path"): "FALSE"
}



highlight_edges = []
highlight_nodes = []

if EXECUTED_PATH:

    branch = EXECUTED_PATH[0]

    if branch == "Positive":

        highlight_edges = [
            ("Start", c1),
            (c1, "Positive Path"),
            ("Positive Path", "End")
        ]

        highlight_nodes = [
            "Start",
            c1,
            "Positive Path",
            "End"
        ]

    elif branch == "Negative":

        highlight_edges = [
            ("Start", c1),
            (c1, c2),
            (c2, "Negative Path"),
            ("Negative Path", "End")
        ]

        highlight_nodes = [
            "Start",
            c1,
            c2,
            "Negative Path",
            "End"
        ]

    elif branch == "Zero":

        highlight_edges = [
            ("Start", c1),
            (c1, c2),
            (c2, "Zero Path"),
            ("Zero Path", "End")
        ]

        highlight_nodes = [
            "Start",
            c1,
            c2,
            "Zero Path",
            "End"
        ]



node_colors = []

for node in G.nodes():

    if node in highlight_nodes:
        node_colors.append("red")
    else:
        node_colors.append("skyblue")


plt.figure(figsize=(12, 8))

nx.draw_networkx_nodes(
    G,
    pos,
    node_color=node_colors,
    node_size=3500
)

nx.draw_networkx_labels(
    G,
    pos,
    font_size=9,
    font_color="black"
)

nx.draw_networkx_edges(
    G,
    pos,
    edge_color="black",
    arrows=True
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=10
)

if highlight_edges:

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=highlight_edges,
        edge_color="red",
        width=4,
        arrows=True
    )

plt.title("Control Flow Graph (Executed Path Highlighted)")
plt.axis("off")
plt.show()