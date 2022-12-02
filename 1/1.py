def file_input(addr):
    return addr.readlines()
    
def group_numbers(list):
    lists = [[]]
    for i in list:
        if i == "\n":
            lists.append([])
        else:
            lists[-1].append(i)
    return [[item.strip() for item in group] for group in lists]

def sum_list(list):
    temp_list = list
    temp_list = [[int(item) for item in group] for group in temp_list]
    return [sum(a) for a in temp_list]
#Part 1
with open('input.txt') as f:
    #print(max(sum_list(group_numbers(file_input(f)))))

#Part 2
    sorted_list = sorted(sum_list(group_numbers(file_input(f))))
    print(sum(sorted_list[-3:]))