# credit /2024_day_2_solutions (reddit)
test_input = arrays = [
    [7, 6, 4, 2, 1],               # Case 1
    [1, 2, 7, 8, 9],               # Case 2 FAIL
    [9, 7, 6, 2, 1],               # Case 3 FAIL
    [1, 3, 2, 4, 5],               # Case 4 
    [8, 6, 4, 4, 1],               # Case 5 
    [1, 3, 6, 7, 9]                # CASE 6 
]

import math
file_path = "input.txt"
input = []

with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split(" ")
        input.append(
            list(map(int, line.strip().split()))
        )

def is_safe(row):
    readings = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    # look for subset of readings
    # postive scores increase; negative scores decrease
    if set(readings) <= {1, 2, 3} or set(readings) <= {-1, -2, -3}:
        return True
    return False

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in input])
print(safe_count)
























'''
def get_pair(col_count:int, pos:int):
    cur = pos
    next = (cur + 1) if (cur + 1) <= (col_count - 1) else -1
    return cur, next

for row in test_input:
    col_count = len(row)
    first_row = True
    first_score = row[0] - row[1]
    start_dir = None if first_score == 0 else 'INC' if first_score < 0 else 'DEC'
    safe = True
    scores = []

    # calc scores
    for pos in range(col_count):
        cur, next = get_pair(col_count, pos)
        score = first_score if first_row else (row[cur] - row[next])

        # end of data check
        if next == -1: 
            break

        # calculate direction
        scores.append(score)
        if start_dir is None:
            start_dir = None if score == 0 else 'INC' if score < 0 else 'DEC'
        first_row = False
    print ("")
    print (f"{start_dir}     {row} | {scores}")

    # safety test (max threshold)
    safe = ( 
        len([v for v in scores if abs(v) > 3]) == 0  
    )
    print (f"{start_dir} MAX {row} | {scores} | {safe}")

    # safety test (no data readings)
    missing_readings = scores.count(0)
    if safe:
        safe = scores.count(0) < 2
    print (f"{start_dir} CNT {row} | {scores} | {safe}")

    # direction safey tests
    if safe and missing_readings == 0:
        # no missing readings and less than single dir change
        hits = 0
        if start_dir == 'DEC':
            hits = len([v for v in scores if abs(v) < 0])
        else: #'INC'
            hits = len([v for v in scores if v < 0])
        
        safe = hits >= len(scores) - 1
        print (f"{start_dir} DIR {row} | {scores} | {safe}")
    
    else: # check adjacent values for missing readings
        continue

    print ("")

    #print (f"{start_dir} {scores} {safe}")
'''

''''
answer = 0
for row in test_input:
    first_row = True
    first_score = row[0] - row[1]
    start_up = None if first_score == 0 else True if first_score < 0 else False
    skip_level_counter = 0
    col_count = len(row)
    cur, next = 0, 0
    safe = True
    for pos in range(col_count):
        # set index pairs
        cur = pos
        next = cur + 1 if (cur + 1) <= (col_count - 1) else -1
        score = first_score if first_row else (row[cur] - row[next])
        first_row = False

        # end of data check
        if next == -1: 
            break
        
        # never safe
        if (abs(score) > 3):
            print ("Hit a")
            safe = False
            break
        
        # no level change check
        if score == 0:
            skip_level_counter += 1
            print ("Hit b")
            continue

        # trend test - init start direction
        if start_up is None:
            start_up is None if score == 0 else True if first_score < 0 else False

        if start_up is not None:
            # same trend
            if start_up and score < 0:
                print ("Hit c")
                continue
            
            # peek next level
            cur = next
            next = (cur + 1) if (cur + 1) <= (col_count -1) else -1
            peek_score = score if next == -1 else (row[cur] - row[next])
            #if peek_score is None: 
            #    print ("hit d")
            #    continue
            print (f"start_up={start_up} peek_score={peek_score} cur_score={score} skip={skip_level_counter}")
            # started increasing and then trended down
            if (start_up and score > 0): # and peek_score < 0:
                print ("Hit e")
                skip_level_counter += 1
            # started decreasing and then trended up
            elif (not start_up and score < 0): # and peek_score > 0:
                print ("Hit f")
                skip_level_counter += 1
            else:
                print ("Hit G")
                continue

    safe = safe and skip_level_counter <= 1
    #print (f"skip level = {skip_level_counter}")
    
    #skip = "<--- unsafe level skip" if skip_level_counter > 1 else ""
    #msg = f"{row} {skip} counter = {skip_level_counter}"
    #print (msg)

    #if safe and skip_level_counter == 1:
    msg = f"{row} counter = {skip_level_counter}"
    print (msg)
    
   
    answer+= 1 if safe else 0

print (answer)

'''

# 359 too low
# 
# 371 not the right answer
# 383 too high
# 407 too high

