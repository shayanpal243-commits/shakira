import matplotlib.pyplot as plt

print("JENSEN MODEL")

loc = float(input("Enter LOC: "))
ctc = float(input("Enter Technology Constant: "))
t = float(input("Enter Time: "))
cost_year = float(input("Enter Cost per Year: "))

effort = (loc / (ctc * t))**2
staff = effort / t
cost = effort * cost_year

print("Effort:", round(effort,2))
print("Staff:", round(staff,2))
print("Cost:", round(cost,2))


time = []
efforts = []

for i in range(5,51):
    x = i * t / 10
    y = (loc / (ctc * x))**2

    time.append(x)
    efforts.append(y)


plt.plot(time, efforts)

plt.scatter(t, effort)
plt.text(t, effort, "Actual Point")

plt.xlabel("Time")
plt.ylabel("Effort")
plt.title("Jensen Model")

plt.grid()
plt.show()