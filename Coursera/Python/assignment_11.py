import re
print sum(int(i) for i in re.findall("[0-9]+", open("regex_sum_245522.txt", "r").read()))
