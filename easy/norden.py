import matplotlib.pyplot as plt
import math

K = float(input("Enter Total Effort K: "))
td = float(input("Enter Peak Time td: "))

time = []
effort = []

for i in range(1,101):
    t = i * td / 10
    E = (K / td**2) * t * math.exp(-t**2/(2*td**2))

    time.append(t)
    effort.append(E)


peak = (K/td) * math.exp(-0.5)

print("Total Effort:", K)
print("Peak Time:", td)
print("Peak Effort:", round(peak,4))


plt.plot(time, effort)

# Peak marking
plt.scatter(td, peak)
plt.axvline(td, linestyle="--")
plt.text(td, peak, "Peak Time")

plt.xlabel("Time")
plt.ylabel("Effort")
plt.title("Norden Model")

plt.grid()
plt.show()