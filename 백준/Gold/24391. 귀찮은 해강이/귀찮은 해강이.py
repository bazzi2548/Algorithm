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
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]

linked = []
for _ in range(M):
    a, b = map(int, input().split())
    linked.append((a, b))
    if find(a) != find(b):
        union(a, b)

for a, b in linked:
    if find(a) != find(b):
        union(a, b)


_list = list(map(int, input().split()))
now = parent[_list[0]]
answer = 0
for i in range(1, N):
    if now != parent[_list[i]]:
        answer += 1
        now = parent[_list[i]]

print(answer)