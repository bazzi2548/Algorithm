import sys
from collections import deque
input = sys.stdin.readline
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


N = int(input())
_list = [list(input().strip()) for _ in range(N)]
answer = 0

def bfs(x, y):
    _list[x][y] = "."
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]

            if 0<=row<N and 0<=col<N and _list[row][col] == "*":
                _list[row][col] = "."
                q.append((row, col))
    return

for i in range(N):
    for j in range(N):
        if _list[i][j] == "*":
            answer += 1
            bfs(i, j)

print(answer)