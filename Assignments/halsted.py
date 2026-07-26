import tokenize
import math
import keyword
import matplotlib.pyplot as plt

def count_operators_and_operands(file_path):
    operators = []
    operands = []

    with open(file_path, 'rb') as file:
        tokens = tokenize.tokenize(file.readline)

        for token in tokens:
            # Operators
            if token.type == tokenize.OP:
                operators.append(token.string)

            # Keywords treated as operators
            elif token.type == tokenize.NAME and keyword.iskeyword(token.string):
                operators.append(token.string)

            # Identifiers (variables, function names)
            elif token.type == tokenize.NAME:
                operands.append(token.string)

            # Numbers & Strings → operands
            elif token.type in (tokenize.NUMBER, tokenize.STRING):
                operands.append(token.string)

    return operators, operands


def halstead_metrics(N1, N2, n1, n2):
    N = N1 + N2
    n = n1 + n2

    # Avoid log(0)
    if n1 > 0 and n2 > 0:
        N_hat = n1 * math.log2(n1) + n2 * math.log2(n2)
    else:
        N_hat = 0

    V = N * math.log2(n) if n > 0 else 0
    D = (n1 / 2) * (N2 / n2) if n2 > 0 else 0
    E = D * V

    print("\n--- Halstead Metrics ---")
    print(f"Program Length (N): {N}")
    print(f"Estimated Length (N̂): {N_hat:.2f}")
    print(f"Vocabulary (n): {n}")
    print(f"Volume (V): {V:.2f}")
    print(f"Difficulty (D): {D:.2f}")
    print(f"Effort (E): {E:.2f}")

    return {
        "N1": N1, "N2": N2,
        "n1": n1, "n2": n2,
        "N": N, "n": n,
        "V": V, "D": D, "E": E
    }


def plot_graphs(data):
    labels = ['Operators (N1)', 'Operands (N2)']
    values = [data["N1"], data["N2"]]

    plt.figure(figsize=(20, 10))

    # Pie chart
    plt.subplot(1, 2, 1)
    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['blue', 'red'])
    plt.title("Distribution")

    # Bar chart
    plt.subplot(1, 2, 2)
    plt.bar(labels, values, color=['blue', 'red'])
    plt.title("Operators vs Operands")

    
    plt.tight_layout()
    plt.show()


def main():
    file_path = input("Enter the path to the Python file to analyze: ")  # Path to the Python file to analyze

    operators, operands = count_operators_and_operands(file_path)
    ope=["++","--","::"]
    operators.extend(ope)
    
    

    print("\nOperands:", operands)
    print("Operators:", operators)

    N1 = len(operators)
    N2 = len(operands)
    n1 = len(set(operators))
    n2 = len(set(operands))

    data = halstead_metrics(N1, N2, n1, n2)

    # Show graphs
    plot_graphs(data)


if __name__ == '__main__':
    main()