import sys
input = sys.stdin.readline
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

R, C, T = map(int, input().split())
_list = [list(map(int, input().split())) for _ in range(R)]

air = []
for i in range(R):
    if _list[i][0] == -1:
        air.append(i)
def getVisit():
    visit = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            visit[i][j] = _list[i][j]
    return visit

def getCount(x, y):
    temp = []
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]

        if 0<=row<R and 0<=col<C and visit[row][col] != -1:
            temp.append((row, col))
    return temp

def setList(x, y, temp):
    value = visit[x][y] // 5
    _list[x][y] -= (value * len(temp))
    
    for row, col in temp:
        _list[row][col] += value

def propagation(visit):
    for i in range(R):
        for j in range(C):
            if visit[i][j] > 0:
                temp = getCount(i, j)
                setList(i, j, temp)

def clean():
    # 위쪽
    for i in range(air[0]-1, -1, -1):
        if i == air[0] -1 :
            _list[i][0] = 0
        else:
            _list[i+1][0] = _list[i][0]
    _list[0][0] = 0
    _list[0] = _list[0][1:]+[_list[0][0]]
    for i in range(air[0]):
        _list[i][C-1] = _list[i+1][C-1]
    _list[air[0]][C-1] = 0
    _list[air[0]] = [_list[air[0]][0]] + [0] + _list[air[0]][1:-1]
    # 아래쪽
    for i in range(air[1]+1, R-1):
        _list[i][0] = _list[i+1][0]
    _list[R-1][0] = 0
    _list[R-1] = _list[R-1][1:] + [_list[R-1][0]]

    for i in range(R-1, air[1], -1):
        _list[i][C-1] = _list[i-1][C-1]
    _list[air[1]][C-1] = 0
    _list[air[1]] = [_list[air[1]][0]] + [_list[air[1]][-1]] + _list[air[1]][1:-1]
    

for _ in range(T):
    visit = getVisit()
    propagation(visit)
    clean()

def getAnswer():
    answer = 0
    for i in range(R):
        for j in range(C):
            if _list[i][j] > 0:
                answer += _list[i][j]
    print(answer)
getAnswer()
