import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    _list =[]
    for _ in range(N):
        _list.append(list(map(int, input().split())))
    _list.sort()
    
    second = _list[0][1]
    answer = N
    for i in range(1, N):
        if _list[i][1] >= second:
            answer -= 1
        else:
            second = _list[i][1]
            
    print(answer)