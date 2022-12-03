from aocd import lines,submit
sum_1 = 0
sum_2 = 0
test = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']

for row in lines:
    x = len(row)
    ruck_item_1 = slice(0,len(row)//2)
    ruck_item_2 = slice(len(row)//2,len(row))
    has_been_added = []
    for char in row[ruck_item_1]:
        if char in row[ruck_item_2] and char.islower() and char not in has_been_added:
            sum_1 += (ord(char) - 96)
            has_been_added.append(char)
        if char in row[ruck_item_2] and char.isupper() and char not in has_been_added:
            sum_1 += (ord(char) - 64) + 26
            has_been_added.append(char)
#submit(sum_1,part='a',day=3,year=2022)
for i in range(0, len(lines),3):
    for char in lines[i]:
        if (char in lines[i+1]) and (char in lines[i+2]) and char.islower():
            sum_2 += (ord(char) - 96)
            break
        if (char in lines[i+1]) and (char in lines[i+2]) and char.isupper():
            sum_2 += (ord(char) - 64) + 26
            break
submit(sum_2,part='b',day=3,year=2022)