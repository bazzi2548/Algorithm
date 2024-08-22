import sys
input = sys.stdin.readline

n, m = map(int, input().split())
_list = [list(map(int, input().split())) for _ in range(n)]

brushOne = False
brushTwo = False
cnt = 0

for i in range(len(_list)):
    while True:
        for j in range(len(_list[i])):
            if _list[i][j] == 0 and (brushOne == True or brushTwo == True):
                brushOne = False
                brushTwo = False

            if _list[i][j] == 1 and brushOne == False and brushTwo == False:
                brushOne = True
                _list[i][j] -= 1
                cnt += 1

            elif _list[i][j] == 2 and brushOne == False and brushTwo == False:
                brushTwo = True
                _list[i][j] -= 2
                cnt += 1
    
            elif _list[i][j] == 1 and brushOne == True:
                _list[i][j] -= 1
    
            elif _list[i][j] == 2 and brushTwo == True:
                _list[i][j] -= 2
    
        brushOne = False
        brushTwo = False

        if sum(_list[i]) == 0:
            break

print(cnt)