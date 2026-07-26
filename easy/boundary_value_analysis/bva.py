import ast

with open("E:\.dir_bin\easy\boundary_value_analysis\input.py") as f:
    tree = ast.parse(f.read())

print("BOUNDARY VALUE ANALYSIS")

for node in ast.walk(tree):

    if isinstance(node, ast.If):

        print("\nCondition:", ast.unparse(node.test))

        if isinstance(node.test, ast.BoolOp):

            c1 = node.test.values[0]
            c2 = node.test.values[1]

            a = int(ast.unparse(c1.comparators[0]))
            b = int(ast.unparse(c2.comparators[0]))

            print("\nBoundary Values")
            print(a-1, "(Valid)")
            print(a, "(Invalid)")
            print(a+1, "(Invalid)")
            print(b-1, "(Invalid)")
            print(b, "(Invalid)")
            print(b+1, "(Valid)")