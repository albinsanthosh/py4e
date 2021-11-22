import re

file = open('regex_sum_779464.txt', 'r+')
ob = file.read()
a = re.findall('[0-9]+',ob)
sum = 0
for i in a:
    sum = sum + int(i)
print(sum)