import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if [n, k] == [0, 0]:
        break
    _list = list(map(int, input().split()))
    Parent = defaultdict(int)

    index = 0
    for i in range(1, n):
        Parent[_list[i]] = _list[index]
        if i < n - 1 and _list[i] + 1 < _list[i + 1]:
            index += 1

    count = 0
    if Parent[Parent[k]]:
        for Node in _list:
            if (Parent[Parent[k]] == Parent[Parent[Node]]) and Parent[Node] != Parent[k]:
                count += 1
    print(count)
