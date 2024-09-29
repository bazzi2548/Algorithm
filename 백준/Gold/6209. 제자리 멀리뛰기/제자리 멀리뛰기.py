import sys
input = sys.stdin.readline

d, n, m = map(int, input().split())
_list = sorted([int(input()) for _ in range(n)] + [d])

def getConut(mid):
    count = 0
    temp = 0
    for i in _list:
        if i - temp >= mid:
            count += 1
            temp = i
    return count

start, end = 0, d
answer = 0
while start <= end:
    mid = (start + end) // 2
    if getConut(mid) >= n - m + 1:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)