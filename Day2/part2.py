def readFile(fileName: str):
    f = open(fileName, "r")
    data = f.read().splitlines()
    return data

def part2(data):
    depth = 0
    horiz_position = 0
    aim = 0
    for idx, val in enumerate(data):
        direction = data[idx].split()[0]
        direction_ammount = int(data[idx].split()[1])
        if direction == "forward":
            horiz_position += direction_ammount
            depth += aim*direction_ammount
        elif direction == "down":
            aim += direction_ammount
            # depth += direction_ammount
        elif direction == "up":
            aim -= direction_ammount
            # depth -= direction_ammount
    final_position = abs(horiz_position) * abs(depth)
    return final_position
    
if __name__ == "__main__":
    data = readFile("Day2/day2_puzzle_input.txt")
    print(part2(data))
    # print(part2(data))