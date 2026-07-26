import matplotlib.pyplot as plt

fp = [
    [3,4,3,7,5,"Low"],
    [4,5,4,10,7,"Average"],
    [6,7,6,15,10,"High"]
]

EI = int(input("Enter EI: "))
EO = int(input("Enter EO: "))
EQ = int(input("Enter EQ: "))
ILF = int(input("Enter ILF: "))
EIF = int(input("Enter EIF: "))

fi = int(input("Enter FI: "))
factor = float(input("Enter FP to KLOC factor: "))
cost_pm = float(input("Enter cost per PM: "))

VAF = 0.65 + 0.01*fi

efforts = []
names = []

for a,b,c,d,e,name in fp:

    UFP = EI*a + EO*b + EQ*c + ILF*d + EIF*e
    AFP = UFP * VAF
    kloc = AFP * factor

    effort = 2.4 * kloc**1.05
    time = 2.5 * effort**0.38
    team = effort/time
    cost = effort*cost_pm

    print("\nComplexity:",name)
    print("UFP:",round(UFP,2))
    print("AFP:",round(AFP,2))
    print("KLOC:",round(kloc,2))
    print("Effort:",round(effort,2))
    print("Time:",round(time,2))
    print("Team:",round(team,2))
    print("Cost:",round(cost,2))

    names.append(name)
    efforts.append(effort)


plt.bar(names, efforts)
plt.xlabel("Complexity")
plt.ylabel("Effort")
plt.title("Function Point Model")
plt.show()