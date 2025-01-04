import sys
from collections import defaultdict
input = sys.stdin.readline

_set = set()
_dict = defaultdict(int)

n = int(input())
_list = [input().strip() for _ in range(n)]
for name in _list:
    answer = ""
    for i in range(len(name)):
        if name[: i + 1] in _set: continue

        if answer == "": answer = name[: i + 1]
        _set.add(name[: i + 1])

    _dict[name] += 1
    if answer == "":
        if _dict[name] == 1:
            answer = name
        else:
            answer = name + str(_dict[name])

    print(answer)