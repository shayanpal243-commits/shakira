import matplotlib.pyplot as plt

data = [
    [2.4, 1.05, 2.5, 0.38, "Organic"],
    [3.0, 1.12, 2.5, 0.35, "Semi-Detached"],
    [3.6, 1.20, 2.5, 0.32, "Embedded"]
]

kloc = float(input("Enter KLOC: "))
cost_pm = float(input("Enter Cost per Person Month: "))

for a,b,c,d,name in data:
    effort = a * kloc**b
    time = c * effort**d
    team = effort / time
    cost = effort * cost_pm

    print("\nMode:", name)
    print("Effort:", round(effort,2))
    print("Development Time:", round(time,2))
    print("Team Size:", round(team,2))
    print("Cost:", round(cost,2))


x = range(1,51)

for a,b,c,d,name in data:
    effort = []
    time = []
    team = []
    cost = []

    for k in x:
        e = a*k**b
        t = c*e**d

        effort.append(e)
        time.append(t)
        team.append(e/t)
        cost.append(e*cost_pm)

    plt.plot(x, effort, label=name)

plt.xlabel("KLOC")
plt.ylabel("Effort")
plt.title("COCOMO Model")
plt.legend()
plt.grid()
plt.show()