import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

n, m = map(int, input().split())
_list = [list(map(str, input().strip())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
wolves = []

for i in range(1, n-1):
    for j in range(1, m-1):
        if _list[i][j] == "W":
            wolves.append((i, j))

def bfs():
    q = deque(wolves)
    for wolf in wolves:
        visit[wolf[0]][wolf[1]] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            row = x + dx[i % 4]
            col = y + dy[i % 4]
            while 0<=row<n and 0<=col<m and _list[row][col] == "+":
                X = row + dx[i]
                Y = col + dy[i]
                if _list[X][Y] != "#":
                    row = X
                    col = Y
                else:
                    break
                
            if 0<=row<n and 0<=col<m and not visit[row][col] and _list[row][col] != "#":
                visit[row][col] = 1
                q.append((row, col))

bfs()

for i in range(1, n-1):
    for j in range(1, m-1):
        if _list[i][j] == "." and not visit[i][j]:
            _list[i][j] = "P"

for i in range(n):
    print(''.join(_list[i]))
