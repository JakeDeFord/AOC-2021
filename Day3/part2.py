from numpy import ones_like


def readFile(fileName: str):
    f = open(fileName, "r")
    data = f.read().splitlines()
    return data

def calc_gamma(data):
    oxy_temp_list = []
    c02_temp_list = []
    data1_list = []
    data2_list = []
    data1 = data
    data2 = data
    for x in range(0, len(data[0])):
        if len(data1) > 1:
            data1_list.append([y[x] for y in data1])
            ones_count = data1_list[x].count('1')
            zeroes_count = data1_list[x].count('0')
            if ones_count >= zeroes_count:
                for y in data1:
                    if y[x] == '1':
                        oxy_temp_list.append(y)   
            else:
                for y in data1:
                    if y[x] == '0':
                        oxy_temp_list.append(y)
            data1 = oxy_temp_list
            oxy_temp_list = []

        if len(data2) > 1:
            data2_list.append([z[x] for z in data2])
            ones_count = 0
            zeroes_count = 0
            ones_count = data2_list[x].count('1')
            zeroes_count = data2_list[x].count('0')
            if ones_count >= zeroes_count:
                for y in data2:
                    if y[x] == '0':
                        c02_temp_list.append(y) 
            else:
                for y in data2:
                    if y[x] == '1':
                        c02_temp_list.append(y)
            data2 = c02_temp_list
            c02_temp_list = []
        
        
    
    data1 = int(''.join(data1),2)
    data2 = int(''.join(data2),2)
    print(data1)
    print(data2)
    return data1, data2

def do_the_work(data):
    gamma,epsilon = calc_gamma(data)
    # epsilon = calc_epsilon(data)
    return gamma*epsilon

if __name__ == "__main__":
    data = readFile("Day3/day3_puzzle_input.txt")
    # calc_gamma(data)
    power_consumption = do_the_work(data)
    print(power_consumption)