import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
_list = sorted(list(map(int, input().split())) + [L])

def getCount(mid):
    start = 0
    cnt = 0
    for i in _list:
        if (i - start) > mid:
            if (i-start)%mid == 0:
                cnt += (i-start)//mid-1
            else:
                cnt += (i-start)//mid
        start = i
    return cnt

start = 1; end = L
answer = 0
while start<=end:
    mid = (start+end)//2
    cnt = getCount(mid)
    if cnt <= M:
        end = mid-1
        answer = mid
    else:
        start = mid+1

print(answer)