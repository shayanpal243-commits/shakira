import matplotlib.pyplot as plt

# Function Point weight matrix
# [EI, EO, EQ, ILF, EIF]
fp_matrix = [
    [3, 4, 3, 7, 5],   # Low complexity
    [4, 5, 4, 10, 7],  # Average complexity
    [6, 7, 6, 15, 10]  # High complexity
]

complexity_names = ["Low", "Average", "High"]
colors = ["blue", "green", "red"]

# Input counts
EI = int(input("Enter number of External Inputs (EI): "))
EO = int(input("Enter number of External Outputs (EO): "))
EQ = int(input("Enter number of External Inquiries (EQ): "))
ILF = int(input("Enter number of Internal Logical Files (ILF): "))
EIF = int(input("Enter number of External Interface Files (EIF): "))

# Value Adjustment Factor
total_fi = int(input("Enter sum of 14 General System Characteristics (0-70): "))
VAF = 0.65 + (0.01 * total_fi)

# FP to KLOC conversion factor
fp_to_kloc = float(input("Enter FP to KLOC conversion factor: "))

cost_per_pm = float(input("Enter cost per person-month: "))

print("\n--- Function Point Estimation ---")

# Graph data container
kloc_values = []
effort_values = []
dev_time_values = []
team_size_values = []
cost_values = []

for i in range(3):

    w_EI, w_EO, w_EQ, w_ILF, w_EIF = fp_matrix[i]

    # UFP
    UFP = (EI * w_EI) + (EO * w_EO) + (EQ * w_EQ) + (ILF * w_ILF) + (EIF * w_EIF)

    # Adjusted FP
    AFP = UFP * VAF

    # Convert to KLOC
    kloc = AFP * fp_to_kloc

    # Basic COCOMO (Organic assumption)
    a, b, c, d = 2.4, 1.05, 2.5, 0.38

    effort = a * (kloc ** b)
    dev_time = c * (effort ** d)
    team_size = effort / dev_time
    total_cost = effort * cost_per_pm

    print("\nComplexity:", complexity_names[i])
    print("UFP:", round(UFP,2))
    print("Adjusted FP:", round(AFP,2))
    print("KLOC:", round(kloc,2))
    print("Effort(Person-Months):", round(effort,2))
    print("Development Time(Months):", round(dev_time,2))
    print("Team Size:", round(team_size,2))
    print("Total Cost:", round(total_cost,2))

    kloc_values.append(kloc)
    effort_values.append(effort)
    dev_time_values.append(dev_time)
    team_size_values.append(team_size)
    cost_values.append(total_cost)

# Graphs
plt.figure()

plt.subplot(2,2,1)
plt.bar(complexity_names, effort_values, color=colors)
plt.title("Effort by Complexity")
plt.ylabel("Effort")

plt.subplot(2,2,2)
plt.bar(complexity_names, dev_time_values, color=colors)
plt.title("Development Time")

plt.subplot(2,2,3)
plt.bar(complexity_names, team_size_values, color=colors)
plt.title("Team Size")

plt.subplot(2,2,4)
plt.bar(complexity_names, cost_values, color=colors)
plt.title("Total Cost")

plt.tight_layout()
plt.show()