import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(n):
    _list = list(map(int, input().split()))
    graph[_list[0]] = sorted(_list[1:-1])
    
root = int(input())
tree = [[0, 0] for _ in range(n+1)]

def dfs(now, cnt):
    tree[now][0] = cnt
    for next in graph[now]:
        if not tree[next][0]:
            cnt = dfs(next, cnt+1)
    tree[now][1] = cnt+1
    return cnt+1
dfs(root, 1)

for i in range(1, n+1):
    print(i, *tree[i])