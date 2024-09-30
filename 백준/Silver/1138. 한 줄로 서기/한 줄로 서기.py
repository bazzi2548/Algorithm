import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
_list = [0] + list(map(int, input().split()))
def check(idx, __list):
    if idx == N:
        return True
    
    cnt = 0
    for i in range(N):
        if __list[i] == __list[idx]:
            if cnt != _list[__list[idx]]:
                return False
            else:
                break

        if __list[i] > __list[idx]:
            cnt += 1
        
    return check(idx+1, __list)

for i in permutations([i for i in range(1, N+1)], N):
    if check(0, i):
        print(*i)
        break