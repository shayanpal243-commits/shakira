import ast



with open("equivalent_class_partitioning/input.py", "r") as f:
    code = f.read()

tree = ast.parse(code)


for node in ast.walk(tree):

    if not isinstance(node, ast.If):
        continue

    condition = ast.unparse(node.test)

    print("\nCondition Found:")
    print(condition)


    if isinstance(node.test, ast.BoolOp):

        values = node.test.values

        if len(values) == 2:

            c1 = values[0]
            c2 = values[1]

            if (
                isinstance(c1, ast.Compare)
                and isinstance(c2, ast.Compare)
            ):

                var1 = ast.unparse(c1.left)
                var2 = ast.unparse(c2.left)

                if var1 == var2:

                    op1 = c1.ops[0]
                    op2 = c2.ops[0]

                    try:

                        val1 = int(ast.unparse(c1.comparators[0]))
                        val2 = int(ast.unparse(c2.comparators[0]))

                        # age > 18 OR age < 0

                        if isinstance(op1, ast.Gt) and isinstance(op2, ast.Lt):

                            print("\nVALID EQUIVALENCE CLASS")
                            print(
                                f"EC1 : {val2} <= {var1} <= {val1}"
                            )

                            print("\nINVALID EQUIVALENCE CLASSES")
                            print(
                                f"EC2 : {var1} < {val2}"
                            )
                            print(
                                f"EC3 : {var1} > {val1}"
                            )

                            print("\nREPRESENTATIVE TEST CASES")
                            print(
                                f"TC1 = {(val1+val2)//2} (Valid)"
                            )
                            print(
                                f"TC2 = {val2-1} (Invalid)"
                            )
                            print(
                                f"TC3 = {val1+1} (Invalid)"
                            )

                        # marks < 0 OR marks > 100

                        elif isinstance(op1, ast.Lt) and isinstance(op2, ast.Gt):

                            print("\nVALID EQUIVALENCE CLASS")
                            print(
                                f"EC1 : {val1} <= {var1} <= {val2}"
                            )

                            print("\nINVALID EQUIVALENCE CLASSES")
                            print(
                                f"EC2 : {var1} < {val1}"
                            )
                            print(
                                f"EC3 : {var1} > {val2}"
                            )

                            print("\nREPRESENTATIVE TEST CASES")
                            print(
                                f"TC1 = {(val1+val2)//2} (Valid)"
                            )
                            print(
                                f"TC2 = {val1-1} (Invalid)"
                            )
                            print(
                                f"TC3 = {val2+1} (Invalid)"
                            )

                    except:
                        pass

    elif isinstance(node.test, ast.Compare):

        left = ast.unparse(node.test.left)
        op = node.test.ops[0]
        right = ast.unparse(node.test.comparators[0])

        try:
            r = int(right)

            print("\nVALID EQUIVALENCE CLASS")

            if isinstance(op, ast.Gt):

                print(f"EC1 : {left} > {r}")

                print("\nINVALID EQUIVALENCE CLASS")
                print(f"EC2 : {left} <= {r}")

                print("\nREPRESENTATIVE TEST CASES")
                print(f"TC1 = {r+1} (Valid)")
                print(f"TC2 = {r} (Invalid)")

            elif isinstance(op, ast.Lt):

                print(f"EC1 : {left} < {r}")

                print("\nINVALID EQUIVALENCE CLASS")
                print(f"EC2 : {left} >= {r}")

                print("\nREPRESENTATIVE TEST CASES")
                print(f"TC1 = {r-1} (Valid)")
                print(f"TC2 = {r} (Invalid)")

            elif isinstance(op, ast.GtE):

                print(f"EC1 : {left} >= {r}")

                print("\nINVALID EQUIVALENCE CLASS")
                print(f"EC2 : {left} < {r}")

                print("\nREPRESENTATIVE TEST CASES")
                print(f"TC1 = {r} (Valid)")
                print(f"TC2 = {r-1} (Invalid)")

            elif isinstance(op, ast.LtE):

                print(f"EC1 : {left} <= {r}")

                print("\nINVALID EQUIVALENCE CLASS")
                print(f"EC2 : {left} > {r}")

                print("\nREPRESENTATIVE TEST CASES")
                print(f"TC1 = {r} (Valid)")
                print(f"TC2 = {r+1} (Invalid)")

            elif isinstance(op, ast.Eq):

                print(f"EC1 : {left} == {r}")

                print("\nINVALID EQUIVALENCE CLASS")
                print(f"EC2 : {left} != {r}")

                print("\nREPRESENTATIVE TEST CASES")
                print(f"TC1 = {r} (Valid)")
                print(f"TC2 = {r+1} (Invalid)")

        except:
            pass
