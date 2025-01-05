import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

m, n = map(int, input().split())
_list = [list(input().strip()) for _ in range(n)]

s = e = None
objects = []
count = 0

for i in range(n):
    for j in range(m):
        if _list[i][j] == 'S':
            s = (i, j)
        elif _list[i][j] == 'E':
            e = (i, j)
        elif _list[i][j] == 'X':
            objects.append((i, j))
            count += 1

def bfs(start, end):
    visited = [[0] * m for _ in range(n)]
    q = deque([start])
    visited[start[0]][start[1]] = 1
    time = 0
    stop = False

    while q:
        size = len(q)
        while size > 0 and not stop:
            x, y = q.popleft()
            for i in range(4):
                row = x + dx[i]
                col = y + dy[i]
                if 0 <= row < n and 0 <= col < m:
                    if visited[row][col] or _list[row][col] == '#':
                        continue
                    if (row, col) == end:
                        stop = True
                        break
                    visited[row][col] = True
                    q.append((row, col))
            size -= 1
        
        if stop:
            break
        time += 1

    return time + 1

if count == 0:
    print(bfs(s, e))

else:
    result = int(1e9)
    for perm in permutations(range(count)):
        tmp = 0
        tmp += bfs(s, objects[perm[0]])
        
        for i in range(1, len(perm)):
            tmp += bfs(objects[perm[i - 1]], objects[perm[i]])

        tmp += bfs(objects[perm[-1]], e)
        result = min(result, tmp)

    print(result)