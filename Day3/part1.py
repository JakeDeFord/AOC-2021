def readFile(fileName: str):
    f = open(fileName, "r")
    data = f.read().splitlines()
    return data

def calc_gamma(data):
    gamma = [0]*len(data[0])
    epsilon = [0]*len(data[0])
    gamma_list = []
    for x in range(0, len(data[0])):
        gamma_list.append([y[x] for y in data])
        ones_count = gamma_list[x].count('1')
        zeroes_count = gamma_list[x].count('0')
        if ones_count > zeroes_count:
            gamma[x] = '1'
            epsilon[x] = '0'
        else:
            gamma[x] = '0'
            epsilon[x] = '1'
    gamma = int(''.join(gamma),2)
    epsilon = int(''.join(epsilon),2)
    return gamma, epsilon

def calc_epsilon(data):
    epsilon = 0

def do_the_work(data):
    gamma,epsilon = calc_gamma(data)
    # epsilon = calc_epsilon(data)
    return gamma*epsilon

if __name__ == "__main__":
    data = readFile("Day3/day3_puzzle_input.txt")
    # calc_gamma(data)
    power_consumption = do_the_work(data)
    print(power_consumption)