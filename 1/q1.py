import sys


num = 0

for line in sys.stdin:
    num += int(line.rstrip())

print(num)