import sys
from collections import deque
input = sys.stdin.readline
convertStr = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
convertNum = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H"}
dx = (1, -1, 1, -1)
dy = (1, 1, -1, -1)

def bfs(start, end):
    visit = [[0] * 9 for _ in range(9)]
    visit[start[0]][start[1]] = 1
    q = deque()
    q.append((start, [convertNum[start[1]], start[0]], 0))
    
    while q:
        pos, now, cnt = q.popleft()
        if pos == end:
            print(cnt, *now)
            return
        
        for i in range(4):
            row = dx[i] + pos[0]
            col = dy[i] + pos[1]

            while 0<row<9 and 0<col<9:
                if not visit[row][col] and cnt <= 3:
                    visit[row][col] = 1
                    q.append(([row, col], now+[convertNum[col], row], cnt+1))
                row += dx[i]
                col += dy[i]
    
    print("Impossible")

for _ in range(int(input())):
    _list = list(map(str, input().split()))
    start = [int(_list[1]), convertStr[_list[0]]]
    end = [int(_list[3]), convertStr[_list[2]]]
    bfs(start, end)