from math import ceil
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(now, cnt):
    global dist, endpoint, min_t

    if dist < cnt:
        dist = cnt
        endpoint = now
        min_t = visit[now]
    elif dist == cnt and visit[now] < min_t:
        endpoint = now
        min_t = visit[now]

    for nxt, time in graph[now]:
        if visit[nxt] == -1:
            visit[nxt] = visit[now] + time
            dfs(nxt, cnt + 1)


N, T = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append((B, C))
    graph[B].append((A, C))

dist, endpoint, min_t = 0, 0, int(1e9)
visit = [-1] * N
visit[0] = 0
dfs(0, 1)

visit = [-1] * N
dist, min_t = 0, int(1e9)
visit[endpoint] = 0
dfs(endpoint, 1)
print(ceil(min_t / T))