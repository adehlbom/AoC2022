from aocd import lines,submit


#Part 1
sum_handshakes = 0     
for row in lines:
    match row:
        case 'A X':
               sum_handshakes += 1 + 3   
        case 'A Y':
                sum_handshakes += 6 + 2
        case 'A Z':
                sum_handshakes += 3
        case 'B X':
                sum_handshakes += 1
        case 'B Y':
                sum_handshakes += 3 + 2
        case 'B Z':
                sum_handshakes += 6 + 3
        case 'C X':
                sum_handshakes += 6 + 1
        case 'C Y':
                sum_handshakes += 2
        case 'C Z':
                sum_handshakes += 3 + 3
#submit(sum_handshakes,part='a',day=2,year=2022)
#Part 2

sum_p2 = 0
    #X = lose,0
    #Y = draw,3
    #Z = win,6
    #A Rock,1
    #B Paper,2
    #C Scissors,3     
for row in lines:
    match row:
        #ROCK
        #lose choose scissor
        case 'A X':
               sum_p2 += 0 + 3
        #draw choose rock   
        case 'A Y':
                sum_p2 += 3 + 1
        #win choose paper
        case 'A Z':
                sum_p2 += 6 + 2
        #PAPER
        #lose choose rock
        case 'B X':
                sum_p2 += 0 + 1
        #draw choose paper
        case 'B Y':
                sum_p2 += 3 + 2
        #win choose scissor
        case 'B Z':
                sum_p2 += 6 + 3
        #SCISSOR
        #lose choose paper
        case 'C X':
                sum_p2 += 0 + 2
        #draw choose scissor
        case 'C Y':
                sum_p2 += 3 + 3
        #win choose rock
        case 'C Z':
                sum_p2 += 6 + 1
print(sum_p2)

#submit(sum_p2,part='b',day=2,year=2022)
