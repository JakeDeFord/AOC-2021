def readFile(fileName: str):
    f = open(fileName, "r")
    data = f.read().splitlines()
    return data

def part1(data):
    depth = 0
    horiz_position = 0
    for idx, val in enumerate(data):
        direction = data[idx].split()[0]
        direction_ammount = int(data[idx].split()[1])
        if direction == "forward":
            horiz_position += direction_ammount
        elif direction == "down":
            depth += direction_ammount
        elif direction == "up":
            depth -= direction_ammount
    final_position = abs(horiz_position) * abs(depth)
    return final_position
    
if __name__ == "__main__":
    data = readFile("day2_puzzle_input.txt")
    print(part1(data))
    # print(part2(data))