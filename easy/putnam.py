import matplotlib.pyplot as plt

print("PUTNAM MODEL")

loc = float(input("Enter LOC: "))
ck = float(input("Enter Technology Constant: "))
t = float(input("Enter Time: "))
cost_year = float(input("Enter Cost per Year: "))

effort = (loc / (ck * t**(4/3)))**3
staff = effort / t
cost = effort * cost_year

print("Effort:", round(effort,2))
print("Staff:", round(staff,2))
print("Cost:", round(cost,2))


time = []
efforts = []

for i in range(5,51):
    x = i * t / 10
    y = (loc / (ck * x**(4/3)))**3

    time.append(x)
    efforts.append(y)


plt.plot(time, efforts)

plt.scatter(t, effort)
plt.text(t, effort, "Actual Point")

plt.xlabel("Time")
plt.ylabel("Effort")
plt.title("Putnam Model")

plt.grid()
plt.show()