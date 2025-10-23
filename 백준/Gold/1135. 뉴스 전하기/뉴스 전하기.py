import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
parent = list(map(int, input().split()))

for i in range(1, N):
    graph[parent[i]].append(i)

def dfs(node):
    times = []
    for child in graph[node]:
        times.append(dfs(child))
    
    times.sort(reverse=True)
    
    max_time = 0
    cnt = 0
    for time in times:
        cnt += 1
        max_time = max(max_time, time + cnt)
    
    return max_time

print(dfs(0))
