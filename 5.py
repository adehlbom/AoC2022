from aocd import lines


array = [None] * 9


#[R] [P] [W] [N] [M] [P] [R] [Q] [L]

#35
def parse_input():
    master_list = []
    temp_list = []

    for idx,row in enumerate(lines):
        for i in range(9):
            temp_list.append(row[4*(i)+1])
        master_list.append(temp_list)
        temp_list = []
        if idx == 7:
            return master_list



new_list = parse_input()

print(new_list)

for x in new_list:
    print(x[0])
