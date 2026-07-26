import tokenize
import keyword
import math
import matplotlib.pyplot as plt

file = input("Enter Python file: ")

operators = []
operands = []

with open(file, "rb") as f:
    for t in tokenize.tokenize(f.readline):

        if t.type == tokenize.OP:
            operators.append(t.string)

        elif t.type == tokenize.NAME:
            if keyword.iskeyword(t.string):
                operators.append(t.string)
            else:
                operands.append(t.string)

        elif t.type == tokenize.NUMBER or t.type == tokenize.STRING:
            operands.append(t.string)

N1 = len(operators)
N2 = len(operands)
n1 = len(set(operators))
n2 = len(set(operands))

N = N1 + N2
n = n1 + n2

N_hat = n1 * math.log2(n1) + n2 * math.log2(n2)
V = N * math.log2(n)
D = (n1 / 2) * (N2 / n2)
E = D * V

print("\n----- HALSTEAD METRICS -----")
print("Operators (N1):", N1)
print("Operands (N2):", N2)
print("Unique Operators (n1):", n1)
print("Unique Operands (n2):", n2)
print("Program Length (N):", N)
print("Vocabulary (n):", n)
print("Estimated Length:", round(N_hat, 2))
print("Volume:", round(V, 2))
print("Difficulty:", round(D, 2))
print("Effort:", round(E, 2))

plt.figure(figsize=(5,5))
plt.pie(
    [N1, N2],
    labels=["Operators", "Operands"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Halstead Metrics")
plt.show()