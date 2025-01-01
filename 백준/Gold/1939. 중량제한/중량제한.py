import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
_list = sorted([list(map(int, input().split())) for _ in range(M)], key = lambda x: -x[2])
start, end = map(int, input().split())

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for s, e, v in _list:
    if find(s) != find(e):
        union(s, e)

    if find(start) == find(end):
        print(v)
        break