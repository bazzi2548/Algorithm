import sys
from collections import deque

input = sys.stdin.readline
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

board = [list(map(str, input().strip())) for _ in range(12)]
answer = 0


def changeDot(changeList):
    for x, y in changeList:
        board[x][y] = "."


def bfs(x, y, char):
    visit = [[0] * 6 for _ in range(12)]
    visit[x][y] = 1
    q = deque()
    q.append((x, y))
    changeList = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if 0 <= row < 12 and 0 <= col < 6 and not visit[row][col] and char == board[row][col]:
                visit[row][col] = 1
                q.append((row, col))
                changeList.append((row, col))

    if len(changeList) >= 4:
        changeDot(changeList)
        return True

    if check:
        return True
    else:
        return False

def remakeBoard():
    for j in range(6):
        for i in range(11, -1, -1):
            if board[i][j] != ".":
                for idx in range(i, 11):
                    if board[idx + 1][j] == ".":
                        board[idx + 1][j], board[idx][j] = board[idx][j], board[idx + 1][j]
                    else:
                        break

while True:
    check = False
    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] != ".":
                check = bfs(i, j, board[i][j])
    if not check:
        break
    answer += 1
    remakeBoard()
print(answer)