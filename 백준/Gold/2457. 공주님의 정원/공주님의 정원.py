import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
_list = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    _list.append([a*100 + b, c*100 + d])

_list = deque(sorted(_list))
start = 301
end = 0
cnt = 0
while _list:
    if start >= 1201 or _list[0][0] > start:
        break

    for _ in range(len(_list)):
        if start>=_list[0][0]:
            if end<=_list[0][1]:
                end = _list[0][1]
            _list.popleft()
        else:
            break
    start = end
    cnt += 1

print(0) if start <= 1130 else print(cnt)