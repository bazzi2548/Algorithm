import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
_list = [int(input()) for _ in range(M)] + [L]

def getCount(mid):
    cnt, temp = 0, 0
    for i in _list:
        if i - temp >= mid:
            cnt += 1
            temp = i
    
    return cnt

for cnt in [int(input()) for _ in range(N)]:
    start, end = 1, L
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        count = getCount(mid)    

        if count > cnt:
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1
    print(answer)