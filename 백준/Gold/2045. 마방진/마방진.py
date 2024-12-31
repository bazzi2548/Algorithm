import sys
input = sys.stdin.readline

_list = [list(map(int,input().split())) for _ in range(3)]
def find_all(_list):
    total_list = [_list[0], _list[1], _list[2]]
    total_list.append([_list[0][0], _list[1][0], _list[2][0]])
    total_list.append([_list[0][1], _list[1][1], _list[2][1]])
    total_list.append([_list[0][2], _list[1][2], _list[2][2]])
    total_list.append([_list[0][0], _list[1][1], _list[2][2]])
    total_list.append([_list[0][2], _list[1][1], _list[2][0]])
    
    answer = sorted(total_list, key=lambda x:x.count(0))[0]
    if 0 in answer:
        return (sum(_list[0]) + sum(_list[1]) + sum(_list[2]))/2
    return sum(answer)

total = int(find_all(_list))

while True:
    for i in range(3):
        if _list[i].count(0) == 1:
            _list[i][_list[i].index(0)] = total - sum(_list[i])
    rotate_list = list(map(list, zip(*_list[::-1])))
    for i in range(3):
        if rotate_list[i].count(0) == 1:
            rotate_list[i][rotate_list[i].index(0)] = total - sum(rotate_list[i])
    _list = list(map(list, zip(*rotate_list)))[::-1]

    for i in range(3):
        if 0 in _list[i]:
            continue
    else: 
        break

for i in range(3):
    print(*_list[i])