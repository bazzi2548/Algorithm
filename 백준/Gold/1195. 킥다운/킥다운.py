import sys
input = sys.stdin.readline

first = input().strip()
second = input().strip()

if len(first) > len(second):
    first, second = second, first

meet_thing = 0
for k in range(len(first)):
    for i in range(k+1):
        if first[-k+i-1] == '2' and second[i] == '2':
            break
    else:
        meet_thing = max(meet_thing, k + 1)

    for i in range(k+1):
        if first[i] == '2' and second[-k+i-1] == '2':
            break
    else:
        meet_thing = max(meet_thing, k + 1)

for k in range(len(second) - len(first) + 1):
    for i in range(len(first)):
        if first[i] == '2' and second[i + k] == '2':
            break
    else:
        meet_thing = max(meet_thing, len(first))
        break
print(len(first) + len(second) - meet_thing)
