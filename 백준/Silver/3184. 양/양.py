import sys
from collections import deque
input = sys.stdin.readline
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

R, C = map(int, input().split())
_list = [list(map(str, input().strip())) for _ in range(R)]
visit = [[0] * C for _ in range(R)]
answer = [0, 0]

def bfs(x, y):
    visit[x][y] = 1
    q = deque()
    q.append((x, y))
    sheep = 0
    wolf = 0
    
    if _list[x][y] == "o":
        sheep += 1
    elif _list[x][y] == "v":
        wolf += 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if 0<=row<R and 0<=col<C and not visit[row][col] and _list[row][col] != "#":
                if _list[row][col] == "o":
                    sheep += 1
                elif _list[row][col] == "v":
                    wolf += 1
                visit[row][col] = 1
                q.append((row, col))
    if sheep > wolf:
        answer[0] += sheep
    else:
        answer[1] += wolf
    
    return
for i in range(R):
    for j in range(C):
        if not visit[i][j] and _list[i][j] != "#":
            bfs(i, j)

print(*answer)