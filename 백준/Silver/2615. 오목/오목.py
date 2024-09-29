import sys
input = sys.stdin.readline

dx = (0, 1, 1, -1)
dy = (1, 0, 1, 1)

_list = [list(map(int, input().split())) for _ in range(19)]

def check(color, x, y):
    for i in range(4):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < 19 and 0 <= ny < 19 and _list[nx][ny] == color:
            cnt += 1
            if cnt == 5:
                if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and _list[x - dx[i]][y - dy[i]] == color:
                    break
                if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and _list[nx + dx[i]][ny + dy[i]] == color:
                    break
                return True
            nx += dx[i]
            ny += dy[i]
    return False

def getAnswer():
    for x in range(19):
        for y in range(19):
            if _list[x][y] != 0:
                if check(_list[x][y], x, y):
                    print(_list[x][y])
                    print(x+1, y+1)
                    return
    print(0)

getAnswer()