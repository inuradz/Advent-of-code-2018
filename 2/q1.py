import sys
from collections import defaultdict

input_processed = []

for line in sys.stdin:
    a = line.rstrip()
    d = defaultdict(lambda : 0)
    for l in a:
        d[l] += 1
    input_processed.append(d)

print(input_processed)
