
'''
test_input = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]
'''
import math
file_path = "input.txt"
input = []

with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split(" ")
        input.append(
            list(map(int, line.strip().split()))
        )

answer = 0
for row in input:
    safe = False
    increasing = (row[0] - row[1] < 0)
    col_count = len(row)
    cur, next = 0, 0
    for pos in range(col_count):
        # set index pairs
        cur = pos
        next = cur + 1 if (cur + 1) <= (col_count - 1) else -1
        if next == -1: 
            break    # end of data

        score = row[cur] - row[next]
        is_up_trend = True if score < 0 else False
        no_change = row[cur] == row[next]
        if (abs(score) > 3 or score == 0 or no_change or increasing != is_up_trend):
            safe = False
            break
        safe = True

    # tally safe reports
    answer +=1 if safe else 0

print (answer)