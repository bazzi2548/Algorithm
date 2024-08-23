import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
_dict = {"Baba": []}

for _ in range(n):
    key, value = input().rstrip().split(" is ")
    if key not in _dict:
        _dict[key] = [value]
    else:
        _dict[key].append(value)

_set = set()
for _ in range(len(_dict["Baba"])):
    next_key = _dict["Baba"].pop()
    _set.add(next_key)
    q = deque()
    q.append(next_key)
    
    while q:
        key = q.popleft()
        if key not in _dict:
            continue

        for item in _dict[key]:
            if item in _set:
                continue
            _set.add(item)
            q.append(item)

print('\n'.join(sorted(list(_set))))