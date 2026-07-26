import matplotlib.pyplot as plt

# COCOMO coefficient matrix [a, b, c, d]
kloc_matrix = [
    [2.4, 1.05, 2.5, 0.38],   # Organic
    [3.0, 1.12, 2.5, 0.35],   # Semi-detached
    [3.6, 1.20, 2.5, 0.32]    # Embedded
]

mode_names = ["Organic", "Semi-Detached", "Embedded"]
colors = ["blue", "green", "red"]

kloc = float(input("Enter KLOC (Kilo Lines of Code): "))
cost_per_pm = float(input("Enter cost per person-month: "))

print("\n--- COCOMO Estimation ---")

# Calculate output for each mode
for i in range(3):
    a, b, c, d = kloc_matrix[i]

    effort = a * (kloc ** b)
    development_time = c * (effort ** d)
    team_size = effort / development_time
    total_cost = effort * cost_per_pm

    print("\nMode:", mode_names[i])
    print("Estimated Effort(Person-Months):", round(effort, 2))
    print("Development Time(Months):", round(development_time, 2))
    print("Team size (Persons):", round(team_size, 2))
    print("Total estimated cost:", round(total_cost, 2))


# Graph data
kloc_values = list(range(1, 51))

plt.figure()

for i in range(3):
    a, b, c, d = kloc_matrix[i]

    effort_values = []
    dev_time_values = []
    team_size_values = []
    cost_values = []

    for k in kloc_values:
        e = a * (k ** b)
        t = c * (e ** d)
        p = e / t
        cost = e * cost_per_pm

        effort_values.append(e)
        dev_time_values.append(t)
        team_size_values.append(p)
        cost_values.append(cost)

    plt.subplot(2,2,1)
    plt.plot(kloc_values, effort_values, color=colors[i], label=mode_names[i])
    plt.xlabel("KLOC")
    plt.ylabel("Effort")
    plt.title("KLOC vs Effort")
    plt.grid(True)

    plt.subplot(2,2,2)
    plt.plot(kloc_values, dev_time_values, color=colors[i], label=mode_names[i])
    plt.xlabel("KLOC")
    plt.ylabel("Development Time")
    plt.title("KLOC vs Development Time")
    plt.grid(True)

    plt.subplot(2,2,3)
    plt.plot(kloc_values, team_size_values, color=colors[i], label=mode_names[i])
    plt.xlabel("KLOC")
    plt.ylabel("Team Size")
    plt.title("KLOC vs Team Size")
    plt.grid(True)

    plt.subplot(2,2,4)
    plt.plot(kloc_values, cost_values, color=colors[i], label=mode_names[i])
    plt.xlabel("KLOC")
    plt.ylabel("Total Cost")
    plt.title("KLOC vs Total Cost")
    plt.grid(True)

for i in range(1,5):
    plt.subplot(2,2,i)
    plt.legend()

plt.tight_layout()
plt.show()