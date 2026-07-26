import matplotlib.pyplot as plt
import numpy as np

print("JENSEN SOFTWARE COST ESTIMATION")

try:
    # Input
    loc = float(input("Enter software size (LOC): "))
    ctc = float(input("Enter technology constant: "))
    time = float(input("Enter development time (years): "))
    cost_per_year = float(input("Enter cost per person-year (Rs.): "))

    # Calculations
    effort = (loc / (ctc * time)) ** 2
    staff = effort / time
    cost = effort * cost_per_year

    # Output
    print("\n----- RESULT -----")
    print("Software Size      :", loc, "LOC")
    print("Technology Constant:", ctc)
    print("Development Time   :", time, "years")
    print("Effort             :", round(effort, 2), "person-years")
    print("Average Staff      :", round(staff, 2), "persons")
    print("Estimated Cost     : Rs.", round(cost, 2))

    # Graph
    x = np.linspace(time * 0.5, time * 3, 100)
    y = (loc / (ctc * x)) ** 2

    plt.plot(x, y)
    plt.scatter(time, effort)
    plt.title("Jensen Model")
    plt.xlabel("Development Time (Years)")
    plt.ylabel("Effort (Person-Years)")
    plt.grid(True)
    plt.show()

except ValueError:
    print("Please enter valid numeric values.")