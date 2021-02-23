import sys


freq_num = 0
number_list = []
freq_set = set()
freq_set.add(freq_num)


for line in sys.stdin:
    number_list.append(int(line.rstrip()))

def get_next_num():
    while True:
        for num in number_list:
            yield num

for num in get_next_num():
    freq_num += num
    if freq_num in freq_set:
        break
    else:
        freq_set.add(freq_num)

print(freq_num)