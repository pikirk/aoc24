file_path = "input.txt"
left = []
right = []

delimeter = "   "
with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split(delimeter)
        if len(values) == 2:
            col1, col2 = map(int, values)
            left.append(col1)
            right.append(col2)

left.sort()
right.sort()
score = 0

for i in range(len(left)): 
    target = left[i] 
    score += ( sum(1 for n in right if n == target) ) * target

print (score)