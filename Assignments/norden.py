import numpy as np
import matplotlib.pyplot as plt

# Inputs
K = float(input("Enter Total Effort K (person-years, e.g. 10): "))
td = float(input("Enter Peak Time t_d (years, e.g. 2): "))

# Time values
t = np.linspace(0.01, 5 * td, 200)

# Norden's Rayleigh formula
E = (K / td**2) * t * np.exp(-t**2 / (2 * td**2))

print("\n--- Norden's Model Output ---")
print(f"Total Effort (K): {K}")
print(f"Peak Time (td): {td}")

# Peak effort formula: (K/td) * e^(-0.5)
E_peak = (K / td) * np.exp(-0.5)
print(f"Peak Effort: {E_peak:.4f}")

# Create figure and axis
fig, ax = plt.subplots()

# Plot curve
ax.plot(t, E, color='black', linewidth=2)

# Axis labels
ax.set_xlabel("Time")
ax.set_ylabel("Effort per unit time")

fig.suptitle("Rayleigh Curve — Norden's Model", fontsize=16, y=0.9, x=0.55)

ax.set_title(
    r"$E(t) = \dfrac{K}{t_d^2} \times t \times e^{-t^2/(2t_d^2)}$",
    fontsize=13,
    pad=5
)

ax.axvline(td, color='red', linestyle='--', linewidth=1.5)
ax.text(td+0.2, max(E)*0.05, "td", color='red')

ax.text(max(t)*0.65, max(E)*0.8,
        f"K = {K}\ntd = {td}",
        bbox=dict(facecolor='white', edgecolor='black'))

ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.92])

plt.savefig("norden.png")
plt.show()