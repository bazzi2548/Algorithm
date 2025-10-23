import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dx = (1,0,-1,0)
dy = (0,1,0,-1)

m, n = map(int, input().split())
_list = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    ways = 0
    for i in range(4):
        row = x+dx[i]
        col = y+dy[i]
        if 0 > row or m <= row:
            continue
        if 0 > col or n <= col:
            continue
        if _list[x][y] <= _list[row][col]:
            continue
        ways += dfs(row, col)

    dp[x][y] = ways
    return dp[x][y]

print(dfs(0, 0))