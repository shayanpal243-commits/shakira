import ast


with open("boundary_value_analysis/input.py", "r") as f:
    code = f.read()

tree = ast.parse(code)

print("BOUNDARY VALUE ANALYSIS")


for node in ast.walk(tree):

    if not isinstance(node, ast.If):
        continue

    print("\nCondition Found:")
    print(ast.unparse(node.test))


    # ---------- RANGE CONDITION ----------
    if isinstance(node.test, ast.BoolOp):

        values = node.test.values

        if len(values) == 2:

            c1 = values[0]
            c2 = values[1]

            if (
                isinstance(c1, ast.Compare)
                and isinstance(c2, ast.Compare)
            ):

                var = ast.unparse(c1.left)

                try:

                    v1 = int(ast.unparse(c1.comparators[0]))
                    v2 = int(ast.unparse(c2.comparators[0]))

                    op1 = c1.ops[0]
                    op2 = c2.ops[0]

                    if isinstance(op1, ast.Lt) and isinstance(op2, ast.Gt):

                        lower = v1
                        upper = v2

                    elif isinstance(op1, ast.Gt) and isinstance(op2, ast.Lt):

                        lower = v2
                        upper = v1

                    else:
                        continue

                    print("\nVALID RANGE")
                    print(f"{lower} <= {var} <= {upper}")

                    print("\nBOUNDARY VALUES")

                    print(f"Lower Boundary : {lower}")
                    print(f"Upper Boundary : {upper}")

                    print("\nVALID BOUNDARY VALUES")
                    print(f"{lower}")
                    print(f"{lower + 1}")
                    print(f"{upper - 1}")
                    print(f"{upper}")

                    print("\nINVALID BOUNDARY VALUES")
                    print(f"{lower - 1}")
                    print(f"{upper + 1}")

                    print("\nBOUNDARY TEST CASES")
                    print(f"TC1 = {lower - 1}  (Invalid)")
                    print(f"TC2 = {lower}      (Valid)")
                    print(f"TC3 = {lower + 1}  (Valid)")
                    print(f"TC4 = {upper - 1}  (Valid)")
                    print(f"TC5 = {upper}      (Valid)")
                    print(f"TC6 = {upper + 1}  (Invalid)")

                except:
                    pass


    # ---------- SINGLE CONDITION ----------
    elif isinstance(node.test, ast.Compare):

        var = ast.unparse(node.test.left)
        op = node.test.ops[0]

        try:

            value = int(ast.unparse(node.test.comparators[0]))

            print("\nBOUNDARY")
            print(value)

            print("\nVALID VALUES")

            if isinstance(op, ast.Gt):

                print(value + 1)

            elif isinstance(op, ast.GtE):

                print(value)

                print(value + 1)

            elif isinstance(op, ast.Lt):

                print(value - 1)

            elif isinstance(op, ast.LtE):

                print(value)

                print(value - 1)

            elif isinstance(op, ast.Eq):

                print(value)

            print("\nINVALID VALUES")

            if isinstance(op, ast.Gt):

                print(value)

                print(value - 1)

            elif isinstance(op, ast.GtE):

                print(value - 1)

            elif isinstance(op, ast.Lt):

                print(value)

                print(value + 1)

            elif isinstance(op, ast.LtE):

                print(value + 1)

            elif isinstance(op, ast.Eq):

                print(value - 1)

                print(value + 1)

            print("\nBOUNDARY TEST CASES")

            print(f"{value-1}")
            print(f"{value}")
            print(f"{value+1}")

        except:
            pass