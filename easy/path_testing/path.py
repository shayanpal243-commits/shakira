import ast
import networkx as nx
import matplotlib.pyplot as plt

with open("E:\\.dir_bin\\easy\\path_testing\\input.py") as f:
    code = f.read()

tree = ast.parse(code)

conditions = []

for node in ast.walk(tree):
    if isinstance(node, ast.If):
        conditions.append(ast.unparse(node.test))

print("PATH TESTING")

print("Decision Nodes:", len(conditions))
print("Cyclomatic Complexity:", len(conditions)+1)

print("\nIndependent Paths")
print("1. Start ->", conditions[0], "-> Positive -> End")
print("2. Start ->", conditions[0], "False ->", conditions[1], "-> Negative -> End")
print("3. Start ->", conditions[0], "False ->", conditions[1], "False -> Zero -> End")

EXECUTED_PATH = []
exec(code, {"EXECUTED_PATH": EXECUTED_PATH})

print("\nExecuted Path:", EXECUTED_PATH[0])

G = nx.DiGraph()

G.add_edges_from([
    ("Start", conditions[0]),
    (conditions[0], "Positive"),
    (conditions[0], conditions[1]),
    (conditions[1], "Negative"),
    (conditions[1], "Zero"),
    ("Positive", "End"),
    ("Negative", "End"),
    ("Zero", "End")
])

colors = []

for node in G.nodes():
    if node == EXECUTED_PATH[0]:
        colors.append("red")
    else:
        colors.append("skyblue")

nx.draw(G, with_labels=True, node_color=colors, node_size=2500, arrows=True)

plt.title("Control Flow Graph")
plt.show()