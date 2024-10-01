import sys
input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))
answer = set(_list)

def dfs(_sum, idx):
    answer.add(_sum)
    if idx == N:
        return

    for i in range(idx+1, N):
        dfs(_sum+_list[i], i)

for i in range(N):
    dfs(_list[i], i)

for i in range(1, int(2e9)):
    if i in answer:
        continue
    else:
        print(i)
        break