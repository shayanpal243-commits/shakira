import ast
import networkx as nx
import matplotlib.pyplot as plt

with open("E:\.dir_bin\easy\data_flow_testing\input.py") as f:
    tree = ast.parse(f.read())

print("DATA FLOW TESTING")

definitions = {}
uses = {}

for node in ast.walk(tree):

    if isinstance(node, ast.Assign):

        var = node.targets[0].id
        definitions.setdefault(var, []).append(node.lineno)

        for x in ast.walk(node.value):
            if isinstance(x, ast.Name):
                uses.setdefault(x.id, []).append(node.lineno)

    elif isinstance(node, ast.If):

        for x in ast.walk(node.test):
            if isinstance(x, ast.Name):
                uses.setdefault(x.id, []).append(node.lineno)

print("\nVariable\tDefined\tUsed")

for var in sorted(set(definitions)|set(uses)):
    print(var,"\t",definitions.get(var,"-"),"\t",uses.get(var,"-"))

print("\nDU Chains")

for var in definitions:
    if var in uses:
        for u in uses[var]:
            print(var,": D(",definitions[var][0],")-> U(",u,")")


# CFG

G = nx.DiGraph()

G.add_edges_from([
    ("Start","1"),
    ("1","2"),
    ("2","3"),
    ("3","4"),
    ("4","5"),
    ("5","End")
])

nx.draw(G,with_labels=True,node_size=2000,arrows=True)

plt.title("Control Flow Graph")
plt.show()