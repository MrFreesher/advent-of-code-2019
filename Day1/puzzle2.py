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
    partialFuel = 0
    fuel = int(mass)
    while(fuel > 0):
        fuel = calculateFuel(fuel)
        if(fuel > 0):
            partialFuel += fuel

    totalFuel += partialFuel
print(totalFuel)
