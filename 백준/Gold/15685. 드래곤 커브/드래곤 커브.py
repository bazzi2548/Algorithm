import sys
input = sys.stdin.readline

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

N = int(input())
allDragonCurv = set()

def makeDragonCurv(g):
    for _ in range(g):
        length = len(dragonCurv)-1
        startX, startY, d = dragonCurv[length]

        for i in range(length, -1, -1):
            startX += direction[d][0]
            startY += direction[d][1]
            x, y, d = dragonCurv[i]

            d = (d+1) % 4
            dragonCurv.append((startX, startY, d))

def addAllDragonCurv():
    for x, y, d in dragonCurv:
        allDragonCurv.add((x, y))
    
    x, y, d = dragonCurv[-1]
    x += direction[d][0]
    y += direction[d][1]
    allDragonCurv.add((x, y))
    
def check(x, y):
    dx = [0, 1, 0, 1]
    dy = [0, 1, 1, 0]
    
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if (row, col) not in allDragonCurv:
            return False
    return True

for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragonCurv = [(x, y, d)]

    makeDragonCurv(g)
    addAllDragonCurv()

answer = 0
for i in range(100):
    for j in range(100):
        if check(i, j):
            answer += 1
print(answer)