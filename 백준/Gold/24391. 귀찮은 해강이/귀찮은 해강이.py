import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(M):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)

_list = list(map(int, input().split()))
now = parent[find(_list[0])]
answer = 0
for i in range(1, N):
    if now != parent[find(_list[i])]:
        answer += 1
        now = parent[find(_list[i])]

print(answer)