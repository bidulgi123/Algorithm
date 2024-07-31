import sys
total = ['A', 'N', 'B', 'C', 'N', 'D', 'N', 'E', 'F', 'N', 'G', 'N']
input = sys.stdin.readline
moves = [int(input()) for i in range(int(input()))]
for i, j in enumerate(total):
    if j != 'N' :
        for move in moves :
            if move < 0 :
                move = move % -12
            else :
                move = move % 12
            i += move 
            if i < 0 : 
                i = 12 + i 
            elif i > 11 :
                i = i - 12
            if total[i] == 'N':
                break
        if total[i] != 'N' :
            print(j, total[i])