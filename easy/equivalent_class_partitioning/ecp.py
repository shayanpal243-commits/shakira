import ast

with open("E:\.dir_bin\easy\equivalent_class_partitioning\\input.py") as f:
    tree = ast.parse(f.read())

print("EQUIVALENT CLASS PARTITIONING")

for node in ast.walk(tree):

    if isinstance(node, ast.If):

        print("\nCondition:", ast.unparse(node.test))

        if isinstance(node.test, ast.BoolOp):

            c1 = node.test.values[0]
            c2 = node.test.values[1]

            a = int(ast.unparse(c1.comparators[0]))
            b = int(ast.unparse(c2.comparators[0]))
            var = ast.unparse(c1.left)

            print("\nValid Class")
            print(f"{b} <= {var} <= {a}")

            print("\nInvalid Classes")
            print(f"{var} < {b}")
            print(f"{var} > {a}")

            print("\nTest Cases")
            print((a+b)//2, "- Valid")
            print(b-1, "- Invalid")
            print(a+1, "- Invalid")