input = ""
file_path = "input.txt"
with open(file_path, "r") as file:
    input = file.readlines()

import re

pattern = r"\bmul\(\d+,\d+\)"
matches = re.findall(pattern, "\n".join(input))
pattern = r"(\d+),(\d+)"
answer = 0
for match in matches:
    answer += sum(int(x[0]) * int(x[1]) for x in re.findall(pattern, match))

print (answer)

