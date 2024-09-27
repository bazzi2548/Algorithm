import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())
height = [0] + list(map(int, input().split()))
_list = [[] for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    _list[a].append(b)
    _list[b].append(a)

def dfs(now):
    if visit[now]:
        return visit[now]
    else:
        visit[now] = 1

    for next in _list[now]:
        if height[now] >= height[next]:
            continue
        visit[now] = max(dfs(next)+1, visit[now])
    return visit[now]

for i in range(1, N+1):
    if not visit[i]:
        dfs(i)

for i in range(1, N+1):
    dfs(i)
    print(visit[i])