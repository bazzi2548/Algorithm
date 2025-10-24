import sys, bisect
input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))
lis = [_list[0]]

for i in _list:
    if lis[-1] < i:
        lis.append(i)
    else:
        idx = bisect.bisect_left(lis, i)
        lis[idx] = i

print(len(lis))