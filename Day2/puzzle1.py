

def readFile():
    data = []
    with open("input.txt") as f:
        data = f.read().split(",")
    return [int(i) for i in data]


def calculate(data):
    pointer = 0

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

    return data


data = readFile()


print(calculate(data))
