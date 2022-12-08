from aocd import numbers,submit

def check_range(input_list):
    sum_1 = 0
    for row in input_list:
        range_1 = list(range(row[0],abs(row[1])+1))
        range_2 = list(range(row[2],abs(row[3])+1))
        if(all(e in range_1 for e in range_2) or all(f in range_2 for f in range_1)):
            sum_1 += 1
    return sum_1
    
submit(check_range(numbers),part='a',day=4,year=2022)


def check_overlap(input_list):
    sum_2 = 0
    for row in input_list:
        range_1 = list(range(row[0],abs(row[1])+1))
        range_2 = list(range(row[2],abs(row[3])+1))
        if(set(range_1) & set(range_2)):
            sum_2 += 1
    return sum_2

submit(check_overlap(numbers),part='b',day=4,year=2022)

