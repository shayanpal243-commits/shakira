"""
1.1 Software Cost Estimation Using KLOC (Basic COCOMO Model)
----------------------------------------------------------------
Estimates Effort, Development Time, and Staff required
based on the size of the software in KLOC (Kilo Lines of Code).
No classes used — purely function-based implementation.
"""

# COCOMO coefficients for the three development modes
COCOMO_COEFFICIENTS = {
    "organic":       (2.4, 1.05, 2.5, 0.38),
    "semi-detached": (3.0, 1.12, 2.5, 0.35),
    "embedded":      (3.6, 1.20, 2.5, 0.32),
}


def get_coefficients(mode):
    """Return (a, b, c, d) constants for the given mode."""
    mode = mode.strip().lower()
    if mode not in COCOMO_COEFFICIENTS:
        raise ValueError("Invalid mode! Choose organic / semi-detached / embedded")
    return COCOMO_COEFFICIENTS[mode]


def calculate_effort(kloc, a, b):
    """Effort in Person-Months"""
    return a * (kloc ** b)


def calculate_time(effort, c, d):
    """Development Time in Months"""
    return c * (effort ** d)


def calculate_staff(effort, time):
    """Average number of staff required"""
    return effort / time


def calculate_cost(effort, cost_per_person_month):
    """Total estimated cost"""
    return effort * cost_per_person_month


def display_results(kloc, mode, effort, time, staff, cost):
    print("\n" + "=" * 55)
    print(f"COCOMO COST ESTIMATION (Using KLOC) — {mode.title()} Mode")
    print("=" * 55)
    print(f"Project Size                : {kloc} KLOC")
    print(f"Estimated Effort             : {round(effort, 2)} Person-Months")
    print(f"Estimated Development Time   : {round(time, 2)} Months")
    print(f"Estimated Staff Required     : {round(staff, 2)} Persons")
    print(f"Estimated Project Cost       : Rs. {round(cost, 2)}")
    print("=" * 55)


def main():
    print("SOFTWARE COST ESTIMATION USING KLOC (BASIC COCOMO)")
    print("Modes available: organic | semi-detached | embedded\n")

    try:
        kloc = float(input("Enter the estimated size of the program (in KLOC): "))
        mode = input("Enter the development mode: ")
        cost_per_pm = float(input("Enter cost per Person-Month (Rs.): "))

        a, b, c, d = get_coefficients(mode)

        effort = calculate_effort(kloc, a, b)
        time = calculate_time(effort, c, d)
        staff = calculate_staff(effort, time)
        cost = calculate_cost(effort, cost_per_pm)

        display_results(kloc, mode, effort, time, staff, cost)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()