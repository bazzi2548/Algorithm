import sys
input = sys.stdin.readline

d, n, m = map(int, input().split())
_list = sorted([int(input()) for _ in range(n)] + [d])

def getCount(mid):
    temp = 0
    tempList = [d]
    for i in _list:
        if i - temp > mid:
            tempList.append(i-temp)
            temp = i
    return tempList

start = 0; end = d
answer = 0

while start<=end:
    mid = (start+end)//2
    tempList = getCount(mid)

    if len(tempList)-1 > n - m:
        start = mid + 1
    else:
        answer = min(mid, min(tempList))
        end = mid - 1

print(answer)
