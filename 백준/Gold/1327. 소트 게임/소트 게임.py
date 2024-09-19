import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
_list = input().split()
visit = set()
answer = sorted(_list)

def sortList(arr, x):
    temp = arr[:]
    temp[x-1:x-1+k] = temp[x-1:x-1+k][::-1]
    return temp

q = deque([(_list, 0)])
while q:
    temp, cnt = q.popleft()
    if temp == answer:
        print(cnt)
        break
    
    for i in range(n-k+1):
        t = sortList(temp, i+1)
        _str = ''.join(t)
        if _str not in visit:
            visit.add(_str)
            q.append((t, cnt+1))

else:
    print(-1)
