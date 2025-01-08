import sys
import heapq
input = sys.stdin.readline

INF = int(2e9)
N, M = map(int, input().split())
_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    _list[a].append([b, c])
X, Y, Z = map(int, input().split())

def includeY(start, target):
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cost, now = heapq.heappop(pq)
        if distance[now] < cost: continue

        for next, val in _list[now]:
            if distance[next] > cost + val:
                distance[next] = cost + val
                heapq.heappush(pq, [cost + val, next])
    return distance[target]

def decludeY(start):
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])
    
    while pq:
        cost, now = heapq.heappop(pq)
        if distance[now] < cost: continue

        for next, val in _list[now]:
            if next == Y: continue
            if distance[next] > cost + val:
                distance[next] = cost + val
                heapq.heappush(pq, [cost + val, next])
    
    return distance[Z]

include = includeY(X, Y) + includeY(Y, Z)
if include >= INF: include = -1

declude = decludeY(X)
if declude >= INF: declude = -1

print(include, declude)