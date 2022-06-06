
def readFile(fileName: str):
    f = open(fileName, "r")
    data = f.read().splitlines()
    data = [ int(x) for x in data ]
    return data


def part1(data):
    previous_depth = data[0]
    larger = 0
    for idx, current_depth in enumerate(data):
        if current_depth > previous_depth:
            larger += 1
        previous_depth = current_depth
    return larger

def part2(data):
    previous_sum = data[0] + data[1] + data[2] 
    larger = 0
    for idx, current_depth in enumerate(data):
        try:
            current_sum = data[idx] + data[idx+1] + data[idx+2]
            if current_sum > previous_sum:
                larger += 1 
        except:
            pass
        previous_sum = current_sum
    return larger



if __name__ == "__main__":
    data = readFile("puzzle_input.txt")
    print(part1(data))
    print(part2(data))