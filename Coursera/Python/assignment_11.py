import re
handle = open("regex_sum_245522.txt", "r")

result = []

for line in handle:
    tmp = re.findall("[0-9]+", line)
    if tmp:
        result += tmp

print sum(int(num) for num in result)