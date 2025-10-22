import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
_list = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    _list[u].append(v)
    _list[v].append(u)

dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1 
    
    for next in _list[node]:
        if not visited[next]:
            dfs(next)
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next][0], dp[next][1])
    
    return

dfs(1)
print(min(dp[1][0], dp[1][1]))