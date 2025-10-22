import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

distance = [None] * (N+1)
_list = [[] for _ in range(N+1)]
def dfs(node):
    distance[node] = 1
    for next in _list[node]:
        if distance[next] == None:
            dfs(next)
            distance[node] += distance[next]
    return 

for _ in range(N-1):
    u, v = map(int, input().split())
    _list[v].append(u)
    _list[u].append(v)

dfs(R)

for _ in range(Q):
    root = int(input())    
    print(distance[root])

