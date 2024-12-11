input = ""
file_path = "input.txt"
with open(file_path, "r") as file:
    input = file.readlines()

import re

# exclude the non-matching group between do() and don't()
pattern = r"(mul\(\d+,\d+\))|(don't\(\))(?:.*?)(mul\(\d+,\d+\))|(do\(\))(?:.*?)(mul\(\d+,\d+\))"
matches = re.findall(pattern, "\n".join(input))
pattern = r"(\d+),(\d+)"
answer = 0
skip = False
mul = ''

for match in matches:
    if not skip and all(e == '' for e in match[1:5]):
        mul = match[0]
    elif not skip and match[1] == "don't()":
        skip = True 
    elif skip and match[3] == "do()":
        skip = False
        mul = match[4]
    elif not skip and match[3] == "do()":
        mul = match[4]

    if not skip:
        answer += sum(int(x[0]) * int(x[1]) for x in re.findall(pattern, mul))
    mul = ''

print (answer)

