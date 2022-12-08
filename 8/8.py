from aocd import get_data
import numpy as np

#print(get_data(day=8,year=2022))
test2 = get_data(day=8, year=2022).split("\n")


test = ['30373',
'25512',
'65332',
'33549',
'35390']

twodlist = []
sumvalues = 0

for line in test2:
    temp_list = []
    for c in line:
        temp_list.append(c)
    twodlist.append(temp_list)
    print(temp_list)


for y in range(1,len(twodlist[0]) - 1):
    line = twodlist[y]
    for x in range(1, len(line) - 1):
        print(x,y)
        rightList = twodlist[y][x+1:]
        leftList = twodlist[y][:x]
        
        column = []
        for temp in twodlist:
            column.append(temp[x])
        uplist = column[:y]
        downlist = column[y+1:]
        currentValue = twodlist[y][x]
        print(rightList)
        print(leftList)
        print(uplist)
        print(downlist)

        okValue = 0
        if(max(rightList) < currentValue):
            okValue = 1
        if(max(leftList) < currentValue):
            okValue = 1
        if(max(uplist) < currentValue):
            okValue = 1
        if(max(downlist) < currentValue):
            okValue = 1

        sumvalues = sumvalues + okValue
        


print(sumvalues)

sumedges = len(twodlist) * 2 + len(twodlist[0])* 2 - 4
print(sumedges)

print(sumvalues + sumedges)
        
        

