import ast
import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

  
# READ SOURCE FILE
  

with open("data_flow_testing/input.py", "r") as f:
    code = f.read()

lines = code.splitlines()

print("DATA FLOW TESTING")

print("\nSOURCE PROGRAM\n")

for i, line in enumerate(lines, start=1):
    print(f"{i:2d} | {line}")

  
# AST ANALYSIS
  

tree = ast.parse(code)

definitions = {}
uses = {}
du_chains = []

  
# VISITOR
  

class DataFlowVisitor(ast.NodeVisitor):

    def visit_Assign(self, node):

        # Definitions
        for target in node.targets:

            if isinstance(target, ast.Name):

                var = target.id

                definitions.setdefault(var, [])
                definitions[var].append(node.lineno)

        # Uses inside assignment expression
        for child in ast.walk(node.value):

            if isinstance(child, ast.Name):

                var = child.id

                uses.setdefault(var, [])
                uses[var].append(node.lineno)

        self.generic_visit(node)

    def visit_If(self, node):

        # Predicate Uses (P-Use)

        for child in ast.walk(node.test):

            if isinstance(child, ast.Name):

                var = child.id

                uses.setdefault(var, [])
                uses[var].append(node.lineno)

        self.generic_visit(node)

    def visit_Name(self, node):

        if isinstance(node.ctx, ast.Load):

            parent = getattr(node, "parent", None)

            if not isinstance(parent, ast.Assign):

                uses.setdefault(node.id, [])

                if node.lineno not in uses[node.id]:
                    uses[node.id].append(node.lineno)

        self.generic_visit(node)


# Parent links

for parent in ast.walk(tree):
    for child in ast.iter_child_nodes(parent):
        child.parent = parent

visitor = DataFlowVisitor()
visitor.visit(tree)

  
# BUILD DU TABLE
  

table = []

all_vars = sorted(
    set(definitions.keys()) | set(uses.keys())
)

for var in all_vars:

    def_lines = definitions.get(var, [])
    use_lines = uses.get(var, [])

    table.append([
        var,
        ", ".join(map(str, def_lines)) if def_lines else "-",
        ", ".join(map(str, use_lines)) if use_lines else "-"
    ])


print("DEFINITION / USE TABLE")


print(
    tabulate(
        table,
        headers=[
            "Variable",
            "Defined At",
            "Used At"
        ],
        tablefmt="grid"
    )
)

  
# DU CHAINS
  


print("DU CHAINS")

for var in all_vars:

    defs = definitions.get(var, [])
    uses_list = uses.get(var, [])

    if defs and uses_list:

        latest_def = defs[0]

        for u in uses_list:

            while (
                len(defs) > 1 and
                defs[1] < u
            ):
                defs.pop(0)

            latest_def = defs[0]

            print(
                f"{var}: D({latest_def}) -> U({u})"
            )

  
# CFG GENERATION
  

G = nx.DiGraph()

G.add_node("Start")

previous = "Start"

node_num = 1

for stmt in tree.body:

    if isinstance(stmt, ast.Assign):

        label = f"{node_num}. Assign"

        G.add_node(label)
        G.add_edge(previous, label)

        previous = label

        node_num += 1

    elif isinstance(stmt, ast.If):

        cond = f"{node_num}. IF"

        G.add_node(cond)
        G.add_edge(previous, cond)

        true_node = f"{node_num}. True"

        G.add_node(true_node)
        G.add_edge(cond, true_node)

        merge = f"{node_num}. Merge"

        G.add_node(merge)

        G.add_edge(true_node, merge)
        G.add_edge(cond, merge)

        previous = merge

        node_num += 1

    else:

        label = f"{node_num}. Statement"

        G.add_node(label)
        G.add_edge(previous, label)

        previous = label

        node_num += 1

G.add_node("End")
G.add_edge(previous, "End")

  
# DRAW CFG
  

plt.figure(figsize=(10, 7))

pos = nx.spring_layout(
    G,
    seed=42
)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    arrows=True,
    font_size=9
)

plt.title("Control Flow Graph (CFG)")
plt.axis("off")

plt.show()