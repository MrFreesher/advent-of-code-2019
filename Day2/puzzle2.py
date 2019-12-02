

def readFile():
    data = []
    with open("input.txt") as f:
        data = f.read().split(",")
    return [int(i) for i in data]


def calculate(data, verb, noun):
    pointer = 0
    data = data[:]
    data[1] = noun
    data[2] = verb
    while True:

        if(data[pointer] == 99):
            break
        elif(data[pointer] == 1):

            data[data[pointer+3]] = data[data[pointer + 2]] + \
                data[data[pointer+1]]
        elif(data[pointer] == 2):

            data[data[pointer + 3]] = data[data[pointer + 2]] * \
                data[data[pointer + 1]]

        pointer += 4

    return data[0]


def findAnswer(data):
    for n in range(100):
        for v in range(100):
            if (calculate(data, v, n) == 19690720):
                return 100 * n + v


data = readFile()
print(findAnswer(data))
