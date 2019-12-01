import math


def calculateFuel(mass):
    if(mass < 0):
        return 0
    else:
        return math.floor(mass/3)-2


totalFuel = 0
masses = []
with open("input.txt") as f:
    masses = f.readlines()

for mass in masses:
    totalFuel += calculateFuel(int(mass))

print(totalFuel)
