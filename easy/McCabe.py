import matplotlib.pyplot as plt

print("McCabe Cyclomatic Complexity")

edges = [
    (1,2),
    (2,3),
    (2,6),
    (3,4),
    (3,5),
    (4,6),
    (5,6),
    (6,7)
]

nodes = []

for a,b in edges:
    if a not in nodes:
        nodes.append(a)
    if b not in nodes:
        nodes.append(b)

E = len(edges)
N = len(nodes)

complexity = E - N + 2

decision = []

for n in nodes:
    count = 0
    
    for a,b in edges:
        if a == n:
            count += 1
            
    if count >= 2:
        decision.append(n)


print("Edges:",E)
print("Nodes:",N)
print("Decision Nodes:",decision)
print("Cyclomatic Complexity:",complexity)
print("Using P+1:",len(decision)+1)


# node positions
pos = {
    1:(1,3),
    2:(2,3),
    3:(3,4),
    4:(4,5),
    5:(4,3),
    6:(5,4),
    7:(6,4)
}


for a,b in edges:
    x = [pos[a][0], pos[b][0]]
    y = [pos[a][1], pos[b][1]]
    plt.plot(x,y,"o-")

for n in nodes:
    plt.text(pos[n][0], pos[n][1], str(n))

plt.title("Control Flow Graph")
plt.grid()
plt.show()