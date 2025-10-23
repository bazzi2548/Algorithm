import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
people = [0] + list(map(int, input().split()))
_list = [[] for _ in range(N+1)]
dp = [[0] * 2 for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    _list[a].append(b)
    _list[b].append(a)

def dfs(node):
    visit[node] = 1
    dp[node][0] = 0
    dp[node][1] = people[node]
    
    for next in _list[node]:
        if visit[next]:
            continue

        dfs(next)
        dp[node][0] += max(dp[next][1], dp[next][0])
        dp[node][1] += dp[next][0]

dfs(1)
print(max(dp[1]))